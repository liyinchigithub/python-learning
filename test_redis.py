#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test_redis.py
# 操作redis key、value、hash
# [python redis 教程]
# https://www.runoob.com/w3cnote/python-redis-intro.html
# https://blog.csdn.net/u013396714/article/details/121233805
# [linux 安装部署redis]
# https://baijiahao.baidu.com/s?id=1722728002073366376&wfr=spider&for=pc


import redis   # 导入redis 模块
import pytest

# 配置信息
redis_info = {
    "host": "121.43.109.207",
    "password": 123456,
    "port": 6379,
    "db": 0
}


@pytest.mark.test
@pytest.mark.L1
def test_redis_Connection():

    try:
        # 创建redis连接池
        pool = redis.ConnectionPool(**redis_info, decode_responses=True) # **redis_info 是一个字典 星号表示把字典所有的键-值对都传入
        # 创建redis连接
        r = redis.Redis(**redis_info,
                        decode_responses=True)
        r.set('name', 'runoob')  # 设置 name 对应的值
        print("r.get('name')",r.get('name'))  # 取出键 name 对应的值
        print(type(r.get('name')))  # 查看类型  <class 'str'>
        
        r.hmset('hash2',{"a":1,"b":2})  # 批量增加（取出）
        print("r.hmget 批量取出所有key的value",r.hmget("hash2", "a", "b"))  # 批量取出"hash2"的key-a b对应的value --方式1  ['1', '2']
        print("r.hget 单个取出指定key的value",r.hget("hash2", "a"))  # 单个取出"hash2"的key-k2对应的value 1
        print("r.hgetall 获取所有键值对",r.hgetall("hash2"))# 获取所有键值对  {'a': '1', 'b': '2'}
        print("r.hlen 得到所有键值对的格式 hash长度",r.hlen("hash2")) # 得到所有键值对的格式 hash长度 2
        print("r.hkeys 得到所有的keys（类似字典的取所有keys）",r.hkeys("hash2"))# 得到所有的keys（类似字典的取所有keys） ['a', 'b']
        print("r.hvals 得到所有的value（类似字典的取所有value）",r.hvals("hash2"))# 得到所有的value（类似字典的取所有value） ['1', '2']
        print("r.hexists 判断成员是否存在（类似字典的in）",r.hexists("hash2", "c"))  # 判断成员是否存在（类似字典的in） False
        
        
        # key是"food" value是"mutton" 将键值对存入redis缓存
        r.set('food', 'mutton', ex=3)# ex - 过期时间（秒）
        print(r.get('food'))  # mutton 取出键food对应的值
    except Exception as e:
        print(e)



'''
    Redis支持五种数据类型：
    string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。
    
    String（字符串）
    string 是 redis 最基本的类型，你可以理解成与 Memcached 一模一样的类型，一个 key 对应一个 value。
    string 类型是二进制安全的。意思是 redis 的 string 可以包含任何数据。比如jpg图片或者序列化的对象。
    string 类型是 Redis 最基本的数据类型，string 类型的值最大能存储 512MB。

    Hash（哈希）
    Redis hash 是一个键值(key=>value)对集合。
    Redis hash 是一个 string 类型的 field 和 value 的映射表，hash 特别适合用于存储对象。

    List（列表）
    Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。

    Set（集合）
    Redis 的 Set 是 string 类型的无序集合。
    集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。

    zset(sorted set：有序集合)
    Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。
    不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。
    zset的成员是唯一的,但分数(score)却可以重复。

'''
