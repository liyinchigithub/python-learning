#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test-MongoDB.py
# 操作数据库MongoDB
# https://www.runoob.com/python3/python-mongodb.html

import pymongo
import pytest


'''
    创建数据库
    注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 
    就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
'''
@pytest.mark.test
def test_create_database():
    client = pymongo.MongoClient("mongodb://localhost:27018/")
    mydb = client["runoobdb"]
    mycol = mydb["sites"]
    print("mycol:{}".format(mycol))


'''
    判断数据库是否已存在
'''
@pytest.mark.test
def test_isexist_database():
    # 注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
    client = pymongo.MongoClient('mongodb://localhost:27018/')
    db_list = client.list_database_names()  # 返回所有数据库名称 类型：list
    # 输出：db_list:['AutoDeploy', 'admin', 'config', 'local', 'runoobdb']
    print("db_list:{}".format(db_list))
    # 判断名称是否在列表汇总
    if "runoobdb" in db_list:
        print("数据库已存在！")
    else:
        print("数据库不存在！")


'''
    [判断集合是否已存在]
'''
@pytest.mark.test
def test_isexist_collection():
    # 注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
    myclient = pymongo.MongoClient('mongodb://localhost:27018/')
    client = myclient['runoobdb']
    col_list = client.list_collection_names()  # 返回指定数据库所有集合的名称 类型：list
    print("col_list:{}".format(col_list))  # col_list:['sites']
    # 输出
    # 判断 sites 集合是否存在
    if "sites" in col_list:
        print("集合已存在！")
    else:
        print("集合不存在！")


'''
    [插入数据]
    集合中插入文档使用 insert_one() 方法，该方法的第一参数是字典 name => value 对。
    以下实例向 sites 集合中插入文档：
    https://www.runoob.com/python3/python-mongodb-insert-document.html
'''
@pytest.mark.test
def test_insert():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    mydb = client["runoobdb"]
    # 集合
    mycol = mydb["sites"]
    # 待插入的数据记录
    mydict = {"name": "RUNOOB", "alexa": "10000",
              "url": "https://www.runoob.com"}
    # 集合中插入记录 数据类型：字典
    x = mycol.insert_one(mydict)
    print(x)


'''
    [查询数据-查询一条数据]
    MongoDB 中使用了 [find] 和 [find_one] 方法来查询集合中的数据，它类似于 SQL 中的 SELECT 语句。
    
    我们可以使用 find_one() 方法来查询集合中的一条数据。
    查询 sites 文档中的第一条数据：
    https://www.runoob.com/python3/python-mongodb-query-document.html
'''
@pytest.mark.test
def test_findone():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    my_db = client["runoobdb"]
    my_col = my_db['sites']
    res = my_col.find_one()
    # 输出:test_findone:{'_id': ObjectId('61ed2635f2550b867d490206'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}
    print("test_findone:{}".format(res))


'''
    [查询数据-查询集合中所有数据]
    find() 方法可以查询集合中的所有数据，类似 SQL 中的 SELECT * 操作。
    以下实例查找 sites 集合中的所有数据：
    https://www.runoob.com/python3/python-mongodb-query-document.html
'''
@pytest.mark.test
def test_find():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    my_db = client["runoobdb"]
    my_col = my_db['sites']
    res = my_col.find()
    for index in res:
        print("test_find:{}".format(index))


'''
    输出:
    test_find:{'_id': ObjectId('61ed2635f2550b867d490206'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}
    test_find:{'_id': ObjectId('61ed58d7b03a32ad53ffe8f6'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}
    test_find:{'_id': ObjectId('61ed58e5a818b094705a3aeb'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}
    test_find:{'_id': ObjectId('61ed58f621e5a7d89d3c0530'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}
    test_find:{'_id': ObjectId('61ed5913b3542cf4cd2be9d5'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}    
'''


'''
    [根据指定条件查询]
    我们可以在 find() 中设置参数来过滤数据。
    以下实例查找 name 字段为 "RUNOOB" 的数据：
'''
@pytest.mark.test
def test_find_condition():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    my_db = client["runoobdb"]
    # 集合
    my_col = my_db['sites']
    # 查询条件
    query = {"name": "RUNOOB"}
    # 执行查询
    res = my_col.find(query)  # 返回数据字段，仅_id
    # 迭代输出
    for index in res:  # res 数据类型list
        print("test_find_condition:{}".format(index))


'''
    [查询指定字段的数据（仅返回想要的字段）]
    我们可以使用 find() 方法来查询指定字段的数据，将要返回的字段对应值设置为 1。
'''
@pytest.mark.test
def test_find_field():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    my_db = client["runoobdb"]
    my_col = my_db['sites']
    res = my_col.find({}, {"name": 0, "alexa": 0, "_id": 1})  # 返回数据字段，仅_id
    for index in res:  # res 数据类型list
        print("test_find:{}".format(index))

    # 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
    # 以下实例除了 _id 字段外，其他都返回：
'''
    输出
    test_find:{'_id': ObjectId('61ed2635f2550b867d490206')}
    test_find:{'_id': ObjectId('61ed58d7b03a32ad53ffe8f6')}
    test_find:{'_id': ObjectId('61ed58e5a818b094705a3aeb')}
    test_find:{'_id': ObjectId('61ed58f621e5a7d89d3c0530')}
    test_find:{'_id': ObjectId('61ed5913b3542cf4cd2be9d5')}
    test_find:{'_id': ObjectId('61ed5d6c72ae9ed8b0c11709')}
    test_find:{'_id': ObjectId('61ed5daa325d76506dd58f5a')}
    test_find:{'_id': ObjectId('61ed5db1e82058403b3a2d0f')}
    test_find:{'_id': ObjectId('61ed5dc4decfecb67e57dbca')}
    test_find:{'_id': ObjectId('61ed5e116a82136a4182aa5a')}
'''


'''
    [高级查询-操作符]
    查询的条件语句中，我们还可以使用修饰符。
    以下实例用于读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"} :
'''
@pytest.mark.test
def test_find_caozuofu():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    my_db = client["runoobdb"]
    # 集合
    my_col = my_db['sites']
    # 查询条件
    query = {"name": {"$gt": "H"}}
    # 执行查询
    res = my_col.find(query)  # 返回数据字段，仅_id
    # 迭代输出
    for index in res:  # res 数据类型list
        print("test_find_caozuofu:{}".format(index))


'''
    [正则表达式查询]
    我们还可以使用正则表达式作为修饰符。
    正则表达式修饰符只用于搜索字符串的字段。
    以下实例用于读取 name 字段中第一个字母为 "R" 的数据，正则表达式修饰符条件为 {"$regex": "^R"} :
'''
@pytest.mark.test
def test_find_regex():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    my_db = client["runoobdb"]
    # 集合
    my_col = my_db['sites']
    # 查询条件
    query = {"name": {"$regex": "^R"}}  # 以R开头的数据
    # 执行查询
    res = my_col.find(query)  # 返回数据类型 ist
    # 迭代输出
    for index in res:  # res 数据类型list
        print("test_find_regex:{}".format(index))

'''
    [修改数据]
    我们可以在 MongoDB 中使用 update_one() 方法修改文档中的记录。该方法第一个参数为查询的条件，第二个参数为要修改的字段。
    如果查找到的匹配数据多于一条，则只会修改第一条。
    以下实例将 alexa 字段的值 10000 改为 12345
    https://www.runoob.com/python3/python-mongodb-update-document.html
'''
@pytest.mark.test
def test_find_update_one():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    my_db = client["runoobdb"]
    # 集合
    my_col = my_db['sites']
    # 查询条件
    query = { "name": "RUNOOB" }
    newvalues = { "$set": { "alexa": "12345" } }
    # 执行更改
    my_col.update_one(query, newvalues)
    # 输出修改后的  "sites"  集合
    for r in my_col.find():
        print("test_find_update_one:{}".format(r))
        
'''
    [修改数据]
    update_one() 方法只能修匹配到的第一条记录
    如果要修改所有匹配到的记录，可以使用 update_many()。
    以下实例将查找所有以 F 开头的 name 字段，并将匹配到所有记录的 alexa 字段修改为 123：
    https://www.runoob.com/python3/python-mongodb-update-document.html
'''
@pytest.mark.test
def test_find_update_many():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    my_db = client["runoobdb"]
    # 集合
    my_col = my_db['sites']
    # 查询条件
    query = { "name": { "$regex": "^R" } }# 条件（正则表达式） 以R开头的数据
    newvalues = { "$set": { "alexa": "54321" } }
    # 执行更改
    my_col.update_many(query, newvalues)
    # 查询数据
    res=my_col.find();
    # 遍历结果
    for r in res:
        print("test_find_update_many:{}".format(r))
        
      
      
'''
    [删除数据-当个文档（记录）]
    我们可以使用 delete_one() 方法来删除一个文档，该方法第一个参数为查询对象，指定要删除哪些数据。
    https://www.runoob.com/python3/python-mongodb-delete-document.html
'''
@pytest.mark.skip
def test_delete_one():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    my_db = client["runoobdb"]
    # 集合
    my_col = my_db['sites']
    # 查询条件
    query = {"name": "RUNOOB"}
    # 执行查询
    res = my_col.delete_one(query)  # 删除第一条数据，如果存在多条仅删除第一条
    # 迭代输出
    print("test_delete_one:{}".format(res))
'''
    [删除数据-删除多个文档（记录）]
    我们可以使用 delete_many() 方法来删除多个文档，该方法第一个参数为查询对象，指定要删除哪些数据。
    删除所有 name 字段中以 F 开头的文档:
'''
@pytest.mark.skip
def test_delete_many():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    my_db = client["runoobdb"]
    # 集合
    my_col = my_db['sites']
    # 查询条件
    query = {"name":{"$regex": "^R"} }# 条件（正则表达式）以R开头的数据
    # 执行查询
    res = my_col.delete_many(query)  # 删除集合中满足指定条件的数据
    # 迭代输出
    print("test_delete_many:{}".format(res))
'''
    [删除数据]
    删除集合中的所有文档
    delete_many() 方法如果传入的是一个空的查询对象，则会删除集合中的所有文档：
'''
@pytest.mark.skip
def test_delete_many_all():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    my_db = client["runoobdb"]
    # 集合
    my_col = my_db['sites']
    # 无条件
    # 执行查询
    res = my_col.delete_many()  # 删除集合中所有的数据
    # 迭代输出
    print("test_delete_many_all:{}".format(res))

        
''''
    [数据排序-升序]
    sort() 方法可以指定升序或降序排序。
    sort() 方法第一个参数为要排序的字段，第二个字段指定排序规则，1 为升序，-1 为降序，默认为升序。
    https://www.runoob.com/python3/python-mongodb-sort.html
'''
@pytest.mark.test
def test_sort_1():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    my_db = client["runoobdb"]
    # 集合
    my_col = my_db['sites']
    # 查询条件
    query = {"name": "RUNOOB"}
    # 执行查询
    res = my_col.find(query).sort("_id")  # 查询name为RUNOOB的数据，并以字段_id进行升序排序
    # 迭代输出
    for index in res:  # res 数据类型list
        print("test_sort_1:{}".format(index))

''''
    [数据排序-降序]
    https://www.runoob.com/python3/python-mongodb-sort.html
'''
@pytest.mark.test
def test_sort_2():
    client = pymongo.MongoClient(
        "mongodb://localhost:27018/")  # 账号密码也在这个url上面体现
    # 数据库
    my_db = client["runoobdb"]
    # 集合
    my_col = my_db['sites']
    # 查询条件
    query = {"name": "RUNOOB"}
    # 执行查询
    res = my_col.find(query).sort("_id",-1)  # 查询name为RUNOOB的数据，并以字段_id进行降序排序
    # 迭代输出
    for index in res:  # res 数据类型list
        print("test_sort_2:{}".format(index))