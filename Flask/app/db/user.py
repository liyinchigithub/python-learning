#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# https://docs.sqlalchemy.org/en/14/orm/quickstart.html
# SQLAlchemy
from unittest import result
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Date, Time, DECIMAL, Text, create_engine,and_, or_, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid
import sys
sys.path.append('../')
from config import *
# 创建对象的基类:
Base = declarative_base()

# 创建表对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)  # 自增、主键、不为空
    username = Column(String(100), nullable=False)  # 字符串、不为空
    password = Column(String(500), nullable=False)  # 字符串、不为空
    type = Column(String(100), nullable=False)  # 字符串、不为空
    uuid = Column(String(500), nullable=False)  # 字符串、不为空
    is_delete = Column(Boolean, nullable=False)  # 布尔值、不为空
    create_date = Column(DateTime, nullable=False)  # 日期时间、不为空，  数据库自动生成时间戳
    update_date = Column(DateTime, nullable=False)  # 日期时间、不为空，  数据库自动生成时间戳
    # datetime.datetime.now() 获取当前时间

'''
    CREATE TABLE IF NOT EXISTS `user`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `username` VARCHAR(100) NOT NULL COMMENT '账号',
    `password` VARCHAR(500) NOT NULL COMMENT '密码',
    `type` VARCHAR(100) NOT NULL COMMENT '账号类型',
    `uuid` VARCHAR(500) NOT NULL COMMENT '唯一uuid',
    `is_delete` TINYINT NOT NULL COMMENT '是否使用',
    `create_date` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '日期',
    `update_date` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新日期',
    PRIMARY KEY (`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

class UserType(Base):
	__tablename__ = 'usertype'
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String(100), nullable=True)
	integral = Column(Integer)
 

'''
    CREATE TABLE IF NOT EXISTS `usertype`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `title` VARCHAR(100) NOT NULL COMMENT '标题',
    `integral` INT NOT NULL COMMENT 'integral',
    PRIMARY KEY (`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

# 初始化数据库连接: TODO 参数化
engine = create_engine(
        f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()

# [插入一条数据]
# User(username=f"{'liyinchi'}",password='123456', type='1',uuid=str(uuid.uuid4()), is_delete=False)

# [插入多条数据] 循环
for i in range(10):
    # 创建新User对象:
    user = User(username=f"{'liyinchi'+str(i)}",
                        password='123456', type='1',uuid=str(uuid.uuid4()), is_delete=False)
    # 打印
    print(f"{user.username},{user.password},{user.type},{user.uuid},{user.is_delete}")
    # [添加到session]
    session.add(user)
#  [提交到session]
session.commit()

# [插入多条数据] 列表
value_list = [
	User(username=f"{'liyinchi1'}",password='123456', type='1',uuid=str(uuid.uuid4()), is_delete=False),
	User(username=f"{'liyinchi2'}",password='123456', type='1',uuid=str(uuid.uuid4()), is_delete=False),
	User(username=f"{'liyinchi3'}",password='123456', type='1',uuid=str(uuid.uuid4()), is_delete=False),
]
session.add_all(value_list)

# [精确查询]
result1=session.query(User).filter(User.username=="liyinchi1").all()
for r in result1:
    print("r.username",r.username)
    print("r.id:",r.id)
print("精确查询======================")
session.commit()

# 获取多条，只返回第一条
# result1=session.query(User).filter(User.username=="liyinchi1").first()
    
# [模糊查询]
result2=session.query(User).filter(User.username.like('%liyinchi%')).all()
for r in result2:
    print("r.username",r.username)
    print("r.id:",r.id)
result = session.query(func.count(User.id),func.count(User.username)).group_by(User.id).all()
print("func.count(User.id):",result)#  [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]
print("模糊查询======================")
session.commit()

# [查询表所有数据]
result = session.query(User).all()

# [多值匹配（包含）]
result3 =session.query(User).filter(User.username.in_(['liyinchi1','liyinchi2'])).all()
for r in result3:
    print("r.username",r.username)
    print("r.id:",r.id)
print("多值匹配======================")

# [多值不匹配（不包含）]
result4 =session.query(User).filter(~User.username.in_(['liyinchi1','liyinchi2'])).all()
for r in result4:
    print("r.username",r.username)
    print("r.id:",r.id)
print("多值不匹配======================")


# [is null]
result5 =session.query(User).filter(User.username.is_(None)).all()
for r in result5:
    print("r.username",r.username)
    print("r.id:",r.id)
print("为空======================")

# [is not null]
result6 =session.query(User).filter(User.username.isnot(None)).all()
for r in result6:
    print("r.username",r.username)
    print("r.id:",r.id)
print("不为空======================")

# [and]
result7 =session.query(User).filter(User.username.like('%liyinchi%'),User.id>5).all()# 方法一
result7 =session.query(User).filter(and_(User.username.like('%liyinchi%'),User.id>5)).all()# 方法二
result7 =session.query(User).filter(User.username.like('%liyinchi%')).filter(User.id>5).all()# 方法三

for r in result7:
    print("r.username",r.username)
    print("r.id:",r.id)
print("多条件  且 and======================")

# [or]
result8 =session.query(User).filter(or_(User.username.like('%liyinchi%'),User.id>5)).all()# 方法二
for r in result8:
    print("r.username",r.username)
    print("r.id:",r.id)
print("或 or======================")

# [限制返回条数]
result=session.query(User).limit(2).all()
# [限制，类似mysql的limit]
result = session.query(User).filter(User.id>1,User.username.like('%liyinchi%'))[1:3]
print("result",result)
print("限制返回条数======================")

# [指定范围之间 between]
result = session.query(User).filter(User.id.between(1, 3))
print("result",result)
print("指定范围之间 between======================")

# [通配符]
result = session.query(User).filter(User.username.like('liyinchi_'))
result = session.query(User).filter(User.username.like('%liyinchi'))
print("result",result)
print("通配符======================")

# [排序] 默认升序，desc降序
result = session.query(User).order_by(User.id.desc()).all()
print("result",result)# 返回的是一个列表
print("排序======================")


# [分组]
result = session.query(func.count(User.id), func.max(User.id), func.min(User.id)).group_by(User.type).all()
print("result",result)# [(1, 1, 1), (1, 1, 1)]
print("分组======================")

# [连表]
# result = session.query(User).join(UserType, isouter=True) # 内连接取外表的交集   isouter=True表示可以不存在关联的数据
# print("result",result)# [(1, 'liyinchi1', '1', '1'), (2, 'liyinchi2', '1', '1'), (3, 'liyinchi3', '1', '1')]
# print("连表======================")
# result = session.query(User).outerjoin(UserType)# 外连接取外表的并集
# print("result",result)# [(1, 'liyinchi1', '1', '1'), (2, 'liyinchi2', '1', '1'), (3, 'liyinchi3', '1', '1')]
# print("连表======================")

'''

https://www.runoob.com/mysql/mysql-join.html
'''



#  union(去重),union_all(不去重) 2个表需要有共同的字段
s1 = session.query(User.id, User.username)
s2 = session.query(UserType.id, UserType.title)
result = s1.union_all(s2)
print("result",result)# 返回的是一个结果集
print("union======================")

'''
SELECT id FROM `user` WHERE id >1 AND id < 5
UNION
SELECT id FROM `usertype` where id >1 AND id < 5

SELECT id,username FROM `user` WHERE id >1 AND id < 5
UNION ALL
SELECT id,title FROM `usertype` where id >1 AND id < 5

https://www.runoob.com/mysql/mysql-union-operation.html
'''


# [子查询/临时表]   subquery()  label()对查询的字段进行命名    子查询的结果集.c.字段，进行对子查询的结果集进行筛选
# select * from (select * from Usertype where id >= 1) as A;
s3 = session.query(UserType.id, UserType.title).filter(UserType.id>1).subquery()
result = session.query(s3).filter(s3.c.id==2)
print("result",result)# 返回的是一个子查询的结果集
print("子查询======================")

s4 = session.query(UserType.title)
result = session.query(User.id, User.username, s4.filter(User.type==UserType.id).as_scalar())
print("result",result)# 返回的是一个元组，元组的第一个元素是User.id，第二个元素是User.username，第三个元素是s4.filter(User.type==UserType.id).as_scalar()
print("子查询======================")

# [修改一条数据]

# 根据 id 字段修改数据
data = {"uuid": "88888"}
result9 =session.query(User).filter(User.id == 8).update(data)
print("result9:",result9)# 1
print("修改一条数据======================")
session.commit()

# [修改多条数据]

data = {"uuid": "123456"}
result10 =session.query(User).filter(User.id==1).filter(User.id>5).update(data)
print("result10:",result10)# 返回修改的条数
print("修改多条数据======================")
session.commit()


# [删除一条数据]
# result11 =session.query(User).filter(User.id == 1).delete()# 根据id字段，删除指定数据
# print("result11:",result11)# 1表示删除成功，0表示删除失败
# print("删除一条数据======================")
# session.commit()

# [删除多条数据]
# result12 =session.query(User).filter(User.username.like('liyinchi%')).delete(False)
# print("result12:",result12)# 返回删除的条数
# print("删除多条数据======================")
# session.commit()

# [全删]
# result13 =session.query(User).delete()
# session.commit()

'''
func.count:统计行的数量。
func.avg:求平均值。
func.max:求最大值。
func.min:求最小值。
func.sum:求和。
func.distinct:求不重复的值。
func.
'''



