#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test_redis.py
# 操作redis key、value、hash
# [python redis 教程]
# https://www.runoob.com/w3cnote/python-redis-intro.html
# https://blog.csdn.net/u013396714/article/details/121233805
# [linux 安装部署redis]
# https://baijiahao.baidu.com/s?id=1722728002073366376&wfr=spider&for=pc

'''
    [redis]
     redis 是一个 Key-Value 数据库，Value 支持 string(字符串)，list(列表)，set(集合)，zset(有序集合)，hash(哈希类型)等类型
'''

import redis   # 导入redis 模块
import pytest
import time

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
        # **redis_info 是一个字典 星号表示把字典所有的键-值对都传入
        pool = redis.ConnectionPool(**redis_info, decode_responses=True)
        '''
        redis-py 使用 connection pool 来管理对一个 redis server 的所有连接，避免每次建立、释放连接的开销。
        默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数 Redis，这样就可以实现多个 Redis 实例共享一个连接池。
        '''

        # 创建redis连接
        r = redis.Redis(**redis_info,
                        decode_responses=True)
        '''
        [redis 基本命令 String]
        set(name, value, ex=None, px=None, nx=False, xx=False)
        在 Redis 中设置值，默认，不存在则创建，存在则修改。
            参数：
            ex - 过期时间（秒）          这里过期时间是3秒，3秒后p，键food的值就变成None
            px - 过期时间（毫秒）        过期时间（豪秒） 这里过期时间是3豪秒，3毫秒后，键foo的值就变成None
            nx - 如果设置为True，则只有name不存在时，当前set操作才执行
            xx - 如果设置为True，则只有name存在时，当前set操作才执行
        '''
        # -------------[string]-------------
        # set
        r.set('name', 'runoob')  # 设置 name 对应的值
        # key是"food" value是"mutton" 将键值对存入redis缓存，但只保留3秒，三秒后redis缓存自动删除
        r.set('food', 'mutton', ex=3)
        # get
        print("r.get('name')", r.get('name'))  # 取出键 name 对应的值
        print(type(r.get('name')))  # 查看类型  <class 'str'>
        # setnx(name, value)
        print(r.setnx('fruit1', 'banana'))  # fruit1不存在，输出为True
        # setex(name, time, value)
        r.setex("fruit2", 5, "orange")
        time.sleep(5)
        print(r.get('fruit2'))  # 5秒后，取值就从orange变成None
        # psetex(name, time_ms, value)
        r.psetex("fruit3", 5000, "apple")
        time.sleep(5)
        print(r.get('fruit3'))  # 5000毫秒后，取值就从apple变成None
        # mset(*args, **kwargs) [批量设置值]
        r.mget({'k1': 'v1', 'k2': 'v2'})
        r.mset(k1="v1", k2="v2")  # 这里k1 和k2 不能带引号，一次设置多个键值对
        print(r.mget("k1", "k2"))   # 一次取出多个键对应的值
        print(r.mget("k1"))
        # mget(keys, *args) [批量获取值]
        print(r.mget('k1', 'k2'))
        print(r.mget(['k1', 'k2']))
        # 将目前redis缓存中的键对应的值批量取出来
        print(r.mget("fruit", "fruit1", "fruit2", "k1", "k2"))
        # getset(name, value)   [设置新值并获取原来的值]
        print(r.getset("food", "barbecue"))  # 设置的新值是barbecue 设置前的值是beef
        # getrange(key, start, end)
        '''
        获取子序列（根据字节获取，非字符）
                参数：
                name - Redis 的 name
                start - 起始位置（字节）
                end - 结束位置（字节）
                如： "君惜大大" ，0-3表示 "君"
        '''
        r.set("cn_name", "君惜大大")  # 汉字
        # 取索引号是0-2 前3位的字节 君 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
        print(r.getrange("cn_name", 0, 2))
        print(r.getrange("cn_name", 0, -1))  # 取所有的字节 君惜大大 切片操作
        r.set("en_name", "junxi")  # 字母
        # 取索引号是0-2 前3位的字节 jun 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
        print(r.getrange("en_name", 0, 2))
        print(r.getrange("en_name", 0, -1))  # 取所有的字节 junxi 切片操作
        r.setrange("en_name", 1, "ccc")
        print(r.get("en_name"))    # jccci 原始值是junxi 从索引号是1开始替换成ccc 变成 jccci
        # setrange(name, offset, value)
        '''
        修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
            参数：
            offset - 字符串的索引，字节（一个汉字三个字节）
            value - 要设置的值
        '''
        # setbit(name, offset, value)
        '''
        对 name 对应值的二进制表示的位进行操作
            参数：
            name - redis的name
            offset - 位的索引（将值变换成二进制后再进行索引）
            value - 值只能是 1 或 0
            注：如果在Redis中有一个对应： n1 = "foo"，

            那么字符串foo的二进制表示为：01100110 01101111 01101111

            所以，如果执行 setbit('n1', 7, 1)，则就会将第7位设置为1，

            那么最终二进制则变成 01100111 01101111 01101111，即："goo"
        '''
        source = "李银池"
        source = "foo"
        for i in source:
            num = ord(i)
            print(bin(num).replace('b', ''))
        # getbit(name, offset)      获取name对应的值的二进制表示中的某位的值 （0或1）
        print(r.getbit("foo1", 0))  # 0 foo1 对应的二进制 4个字节 32位 第0位是0还是1

        # strlen(name)      返回name对应值的字节长度（一个汉字3个字节）
        print(r.strlen("foo"))  # 4 'goo1'的长度是4
        # incr(self, name, amount=1)        自增 name 对应的值，当 name 不存在时，则创建 name＝amount，否则，则自增。
        r.set("foo", 123)
        print(r.mget("foo", "foo1", "foo2", "k1", "k2"))
        r.incr("foo", amount=1)
        print(r.mget("foo", "foo1", "foo2", "k1", "k2"))
        # append(key, value)   在redis name对应的值后面追加内容
        r.append("name", "haha")    # 在name对应的值junxi后面追加字符串haha
        print(r.mget("name"))

        # -------------[hash]-------------

        # hset(name, key, value)        单个增加--修改(单个取出)--没有就新增，有的话就修改
        r.hset("hash1", "k1", "v1")
        r.hset("hash1", "k2", "v2")
        print(r.hkeys("hash1"))  # 取hash中所有的key
        print(r.hget("hash1", "k1"))    # 单个取hash的key对应的值
        print(r.hmget("hash1", "k1", "k2"))  # 多个取hash的key对应的值
        r.hsetnx("hash1", "k2", "v3")  # 只能新建
        print(r.hget("hash1", "k2"))
        # hmset(name, mapping)      批量增加（取出）        mapping - 字典，如：{'k1':'v1', 'k2': 'v2'}
        r.hmset("hash2", {"k2": "v2", "k3": "v3"})
        # hget(name,key)        在name对应的hash中获取根据key获取value
        '''
        在name对应的hash中获取多个key的值
            参数：
            name - reids对应的name
            keys - 要获取key集合，如：['k1', 'k2', 'k3']
            *args - 要获取的key，如：k1,k2,k3
        '''
        print(r.hget("hash2", "k2"))  # 单个取出"hash2"的key-k2对应的value
        # 批量取出"hash2"的key-k2 k3对应的value --方式1
        print(r.hmget("hash2", "k2", "k3"))
        # 批量取出"hash2"的key-k2 k3对应的value --方式2
        print(r.hmget("hash2", ["k2", "k3"]))
        # hgetall(name) 取出所有的键值对
        print(r.hgetall("hash1"))
        # hlen(name)    得到所有键值对的格式 hash长度
        print(r.hlen("hash1"))  # 获取name对应的hash中键值对的个数
        # hkeys(name)  得到所有的keys（类似字典的取所有keys）
        print(r.hkeys("hash1"))  # 获取name对应的hash中所有的key的值
        # hvals(name)   得到所有的value（类似字典的取所有value）
        print(r.hvals("hash1"))
        # hexists(name, key)    判断成员是否存在（类似字典的in）
        print(r.hexists("hash1", "k4"))  # False 不存在
        print(r.hexists("hash1", "k1"))  # True 存在
        # hdel(name,*keys)  [删除键值对] 将name对应的hash中指定key的键值对删除
        print(r.hgetall("hash1"))
        r.hset("hash1", "k2", "v222")   # 修改已有的key k2
        r.hset("hash1", "k11", "v1")   # 新增键值对 k11
        r.hdel("hash1", "k1")    # 删除一个键值对
        print(r.hgetall("hash1"))
        # hincrby(name, key, amount=1) 自增自减整数(将key对应的value--整数 自增1或者2，或者别的整数 负数就是自减)
        '''
        自增name对应的hash中的指定key的值，不存在则创建key=amount
                参数：
                name - redis中的name
                key - hash对应的key
                amount - 自增数（整数）
        '''
        r.hset("hash1", "k3", 123)
        r.hincrby("hash1", "k3", amount=-1)
        print(r.hgetall("hash1"))
        r.hincrby("hash1", "k4", amount=1)  # 不存在的话，value默认就是1
        print(r.hgetall("hash1"))
        # hincrbyfloat(name, key, amount=1.0)  自增自减浮点数(将key对应的value--浮点数 自增1.0或者2.0，或者别的浮点数 负数就是自减)
        r.hset("hash1", "k5", "1.0")
        r.hincrbyfloat("hash1", "k5", amount=-1.0)    # 已经存在，递减-1.0
        print(r.hgetall("hash1"))
        # 不存在，value初始值是-1.0 每次递减1.0
        r.hincrbyfloat("hash1", "k6", amount=-1.0)
        print(r.hgetall("hash1"))
        # hscan(name, cursor=0, match=None, count=None)  取值查看--分片读取
        '''
        增量式迭代获取，对于数据大的数据非常有用，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆
            参数：
            name - redis的name
            cursor - 游标（基于游标分批取获取数据）
            match - 匹配指定key，默认None 表示所有的key
            count - 每次分片最少获取个数，默认None表示采用Redis的默认分片个数

        '''
        print(r.hscan("hash1"))
        # hscan_iter(name, match=None, count=None)      利用yield封装hscan创建生成器，实现分批去redis中获取数据
        for item in r.hscan_iter('hash1'):
            print(item)
        print(r.hscan_iter("hash1"))    # 生成器内存地址

        r.hmset('hash2', {"a": 1, "b": 2})  # 批量增加（取出）
        # 批量取出"hash2"的key-a b对应的value --方式1  ['1', '2']
        print("r.hmget 批量取出所有key的value", r.hmget("hash2", "a", "b"))
        # 单个取出"hash2"的key-k2对应的value 1
        print("r.hget 单个取出指定key的value", r.hget("hash2", "a"))
        # 获取所有键值对  {'a': '1', 'b': '2'}
        print("r.hgetall 获取所有键值对", r.hgetall("hash2"))
        print("r.hlen 得到所有键值对的格式 hash长度", r.hlen(
            "hash2"))  # 得到所有键值对的格式 hash长度 2
        # 得到所有的keys（类似字典的取所有keys） ['a', 'b']
        print("r.hkeys 得到所有的keys（类似字典的取所有keys）", r.hkeys("hash2"))
        # 得到所有的value（类似字典的取所有value） ['1', '2']
        print("r.hvals 得到所有的value（类似字典的取所有value）", r.hvals("hash2"))
        print("r.hexists 判断成员是否存在（类似字典的in）", r.hexists(
            "hash2", "c"))  # 判断成员是否存在（类似字典的in） False

        # -------------[list]-------------

        # lpush(name,values)    增加（类似于list的append，只是这里是从左边新增加）--没有就新建
        r.lpush("list1", 11, 22, 33)
        print(r.lrange('list1', 0, -1))
        # 增加（从右边增加）--没有就新建
        r.rpush("list2", 44, 55, 66)    # 在列表的右边，依次添加44,55,66
        print(r.llen("list2"))  # 列表长度
        print(r.lrange("list2", 0, -1))  # 切片取出值，范围是索引号0到-1(最后一个元素)

        # [set]
        # sadd(name,values)          新增
        r.sadd("set1", 33, 44, 55, 66)  # 往集合中添加元素
        print(r.scard("set1"))  # 集合的长度是4
        print(r.smembers("set1"))   # 获取集合中所有的成员
        # scard(name)                获取元素个数 类似于len
        print(r.scard("set1"))  # 集合的长度是4
        # smembers(name)            获取集合中所有的成员
        print(r.smembers("set1"))   # 获取集合中所有的成员
        # sscan(name, cursor=0, match=None, count=None) 获取集合中所有的成员--元组形式
        print(r.sscan("set1"))
        # sscan_iter(name, match=None, count=None)      获取集合中所有的成员--迭代器的方式
        for i in r.sscan_iter("set1"):
                print(i)
        # sdiff(keys, *args)                差集
        r.sadd("set2", 11, 22, 33)
        print(r.smembers("set1"))   # 获取集合中所有的成员
        print(r.smembers("set2"))
        print(r.sdiff("set1", "set2"))   # 在集合set1但是不在集合set2中
        print(r.sdiff("set2", "set1"))   # 在集合set2但是不在集合set1中
        # sdiffstore(dest, keys, *args)     差集--差集存在一个新的集合中
        r.sdiffstore("set3", "set1", "set2")    # 在集合set1但是不在集合set2中
        print(r.smembers("set3"))   # 获取集合3中所有的成员     {'11', '22', '33'}
        # sinter(keys, *args)               交集
        print(r.sinter("set1", "set2"))  # 取2个集合的交集
        # sinterstore(dest, keys, *args)    交集--交集存在一个新的集合中
        print(r.sinterstore("set3", "set1", "set2"))  # 取2个集合的交集
        print(r.smembers("set3"))
        # sunion(keys, *args) 并集
        print(r.sunion("set1", "set2"))  # 取2个集合的并集
        # sunionstore(dest,keys, *args)     并集--并集存在一个新的集合
        print(r.sunionstore("set3", "set1", "set2"))  # 取2个集合的并集
        print(r.smembers("set3"))
        # sismember(name, value)        判断是否是集合的成员 类似in
        print(r.sismember("set1", 33))  # 33是集合的成员
        print(r.sismember("set1", 23))  # 23不是集合的成员
        # smove(src, dst, value)          移动
        r.smove("set1", "set2", 44)
        print(r.smembers("set1"))
        print(r.smembers("set2"))
        # spop(name)               删除--随机删除并且返回被删除值
        # 从集合移除一个成员，并将其返回,说明一下，集合是无序的，所有是随机删除的
        print(r.spop("set2"))   # 这个删除的值是随机删除的，集合是无序的
        print(r.smembers("set2"))
        # srem(name, values)          删除--集合指定值删除
        print(r.srem("set2", 11))   # 从集合中删除指定值 11
        print(r.smembers("set2"))
        
        # -------------[有序set]-------------
        # zadd(name, *args, **kwargs)   添加
        r.zadd("zset1", n1=11, n2=22)
        r.zadd("zset2", 'm1', 22, 'm2', 44)
        print(r.zcard("zset1")) # 集合长度
        print(r.zcard("zset2")) # 集合长度
        print(r.zrange("zset1", 0, -1))   # 获取有序集合中所有元素
        print(r.zrange("zset2", 0, -1, withscores=True))   # 获取有序集合中所有元素和分数
        
        # zcard(name)           获取有序集合元素个数 类似于len
        print(r.zcard("zset1")) # 集合长度
        
        # r.zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)  获取有序集合的所有元素
        '''
        按照索引范围获取name对应的有序集合的元素
            参数：
            name - redis的name
            start - 有序集合索引起始位置（非分数）
            end - 有序集合索引结束位置（非分数）
            desc - 排序规则，默认按照分数从小到大排序
            withscores - 是否获取元素的分数，默认只获取元素的值
            score_cast_func - 对分数进行数据转换的函数
            3-1 从大到小排序(同zrange，集合是从大到小排序的)
            zrevrange(name, start, end, withscores=False, score_cast_func=float)
        '''
        print(r.zrevrange("zset1", 0, -1))    # 只获取元素，不显示分数
        print(r.zrevrange("zset1", 0, -1, withscores=True)) # 获取有序集合中所有元素和分数,分数倒序
        # zincrby(name, value, amount)          自增
        r.zincrby("zset3", "n2", amount=2)    # 每次将n2的分数自增2
        print(r.zrange("zset3", 0, -1, withscores=True))
        # zrank(name, value)                    获取值的索引号
        print(r.zrank("zset3", "n1"))   # n1的索引号是0 这里按照分数顺序（从小到大）
        print(r.zrank("zset3", "n6"))   # n6的索引号是1
        print(r.zrevrank("zset3", "n1"))    # n1的索引号是29 这里安照分数倒序（从大到小）
        # zrem(name, values)                    删除--有序集合指定值删除
        r.zrem("zset3", "n3")   # 删除有序集合中的元素n3 删除单个
        print(r.zrange("zset3", 0, -1))
        # zremrangebyrank(name, min, max)        删除--根据排行范围删除，按照索引号来删除
        r.zremrangebyrank("zset3", 0, 1)  # 删除有序集合中的索引号是0, 1的元素
        print(r.zrange("zset3", 0, -1))
        # zremrangebyscore(name, min, max)      删除--根据分数范围删除
        r.zremrangebyscore("zset3", 11, 22)   # 删除有序集合中的分数是11-22的元素
        print(r.zrange("zset3", 0, -1))
        # zscore(name, value)                   获取值对应的分数
        print(r.zscore("zset3", "n27"))   # 获取元素n27对应的分数27
        
        
        #-------------[其他常用操作]-------------
        # 1.delete(*names)          根据删除redis中的任意数据类型（string、hash、list、set、有序set）
        r.delete("gender")  # 删除key为gender的键值对
        # 2.exists(name)            检查名字是否存在
        print(r.exists("zset1"))    # 检测redis的name是否存在，存在就是True，False 不存在
        # 3.keys(pattern='')        模糊匹配
        '''
        根据模型获取redis的name
            KEYS * 匹配数据库中所有 key 。
            KEYS h?llo 匹配 hello ， hallo 和 hxllo 等。
            KEYS hllo 匹配 hllo 和 heeeeello 等。
            KEYS h[ae]llo 匹配 hello 和 hallo ，但不匹配 hillo
        '''
        print(r.keys("foo*"))
        # 4.expire(name ,time)      设置超时时间
        r.lpush("list5", 11, 22)
        r.expire("list5", time=3)
        print(r.lrange("list5", 0, -1))
        time.sleep(3)
        print(r.lrange("list5", 0, -1))
        # 5.rename(src, dst)        重命名
        r.lpush("list5", 11, 22)
        r.rename("list5", "list5-1")
        # 6.type(name)              获取类型
        print(r.type("set1"))
        print(r.type("hash2"))
        # 7.其他
        print(r.get('name'))    # 查询key为name的值
        r.delete("gender")  # 删除key为gender的键值对
        print(r.keys())  # 查询所有的Key
        print(r.dbsize())   # 当前redis包含多少条数据
        r.save()    # 执行"检查点"操作，将数据写回磁盘。保存时阻塞
        # r.flushdb()        # 清空r中的所有数据

        # [管道（pipeline）]

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
