#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# python获取apollo配置文件中的配置项，使用requests库



import json,os
import logging
import sys
import threading
import time
import requests
# sys.path.append("./")

class Apollo():
    def __init__(self, appid, config_server_url):
        self.appid = appid
        self.config_url = config_server_url
        self.apollo = ApolloClient(app_id=self.appid, config_server_url=self.config_url)
        self.apollo.start()

    def get_value(self, key, namespace="application"):
        """
        获取指定appid下指定namespace下的指定key的值
        :param appid: apollo appid
        :param key:
        :param namespace:
        :return: value
        """
        try:
            return self.apollo.get_value(key=key, namespace=namespace)
        except Exception as e:
            return None

    def get_all_values_no_cache(self, appid, namespace="application"):
        """
        通过不带缓存的Http接口从Apollo读取配置
        :return: 指定namespace下的全部数据 dict
        """
        url = '{}/configs/{}/{}/{}?ip={}'.format(self.config_url, appid, "default", namespace, "0.0.0.0")
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()['configurations']
        else:
            return {}



class ApolloClient(object):
    def __init__(self, app_id, cluster='default', config_server_url='http://localhost:8080', interval=60, ip=None):
        self.config_server_url = config_server_url
        self.appId = app_id
        self.cluster = cluster
        self.timeout = 60
        self.interval = interval
        self.init_ip(ip)
        self._stopping = False
        self._cache = {}
        self._notification_map = {'application': -1}

    def init_ip(self, ip):
        if ip:
            self.ip = ip
        else:
            import socket
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('8.8.8.8', 53))
                ip = s.getsockname()[0]
            finally:
                s.close()
            self.ip = ip

    def get_value(self, key, default_val=None, namespace='application', auto_fetch_on_cache_miss=False):
        if namespace not in self._notification_map:
            self._notification_map[namespace] = -1
            logging.getLogger(__name__).info("Add namespace '%s' to local notification map", namespace)

        if namespace not in self._cache:
            self._cache[namespace] = {}
            logging.getLogger(__name__).info("Add namespace '%s' to local cache", namespace)
            self._long_poll()
        if key in self._cache[namespace]:
            return self._cache[namespace][key]
        else:
            if auto_fetch_on_cache_miss:
                return self._cached_http_get(key, default_val, namespace)
            else:
                return default_val

    def start(self):
        if len(self._cache) == 0:
            self._long_poll()
        t = threading.Thread(target=self._listener)
        t.start()

    def stop(self):
        self._stopping = True
        logging.getLogger(__name__).info("Stopping listener...")

    def _cached_http_get(self, key, default_val, namespace='application'):
        url = '{}/configfiles/json/{}/{}/{}?ip={}'.format(self.config_server_url, self.appId, self.cluster, namespace, self.ip)
        r = requests.get(url)
        if r.ok:
            data = r.json()
            self._cache[namespace] = data
            logging.getLogger(__name__).info('Updated local cache for namespace %s', namespace)
        else:
            data = self._cache[namespace]

        if key in data:
            return data[key]
        else:
            return default_val

    def _uncached_http_get(self, namespace='application'):
        url = '{}/configs/{}/{}/{}?ip={}'.format(self.config_server_url, self.appId, self.cluster, namespace, self.ip)
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            self._cache[namespace] = data['configurations']
            logging.getLogger(__name__).info('Updated local cache for namespace %s release key %s: %s',
                                             namespace, data['releaseKey'],
                                             repr(self._cache[namespace]))
    def _long_poll(self):
        url = '{}/notifications/v2'.format(self.config_server_url)
        notifications = []
        for key in self._notification_map:
            notification_id = self._notification_map[key]
            notifications.append({
                'namespaceName': key,
                'notificationId': notification_id
            })

        r = requests.get(url=url, params={
            'appId': self.appId,
            'cluster': self.cluster,
            'notifications': json.dumps(notifications, ensure_ascii=False)
        }, timeout=self.timeout)

        logging.getLogger(__name__).debug('Long polling returns %d: url=%s', r.status_code, r.request.url)

        if r.status_code == 304:
            # no change, loop
            logging.getLogger(__name__).debug('No change, loop...')
            return

        if r.status_code == 200:
            data = r.json()
            for entry in data:
                ns = entry['namespaceName']
                nid = entry['notificationId']
                logging.getLogger(__name__).info("%s has changes: notificationId=%d", ns, nid)
                self._uncached_http_get(ns)
                self._notification_map[ns] = nid
        else:
            logging.getLogger(__name__).warn('Sleep...')
            time.sleep(self.timeout)

    def _listener(self):
        logging.getLogger(__name__).info('Entering listener loop...')
        while not self._stopping:
            self._long_poll()
            time.sleep(self.interval)
        logging.getLogger(__name__).info("Listener stopped!")
        

if __name__ == "__main__":
    apollo = Apollo(appid="test1", config_server_url="http://localhost:8080")
    print("one:", apollo.get_value(key="apollo.portal.envs"))
    # print("one:", apollo.get_value(key="one"))
    # print("name:", apollo.get_value(key="name"))
    # print("age:", apollo.get_value(key="age"))
    # print("values:", apollo.get_all_values_no_cache(appid=102))

"""
输出结果：
one: 1
one: 1
name: 张三
age: None
values: {'one': '1', 'name': '张三'}
"""