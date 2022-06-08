#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# python获取apollo配置文件中的配置项
import json,os,sys
sys.path.append("./")
import pyapollos
import time

def main():
    while 1:
        a = pyapollos.ApolloClient("test1", "default", config_server_url="http://localhost:8070")
        a.start()
        c = a.get_value("apollo.portal.envs")
        print(c)
        time.sleep(2)

if __name__ == '__main__':
    main()

