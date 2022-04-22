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
import sys
sys.path.append('../')
from config import *
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:


class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)  # 自增、主键、不为空
    username = Column(String(100), nullable=False)  # 字符串、不为空
    password = Column(String(500), nullable=False)  # 字符串、不为空
    type = Column(String(100), nullable=False)  # 字符串、不为空
    is_delete = Column(Boolean, nullable=False)  # 布尔值、不为空
    create_date = Column(DateTime, nullable=False)  # 日期时间、不为空，  数据库自动生成时间戳
    update_date = Column(DateTime, nullable=False)  # 日期时间、不为空，  数据库自动生成时间戳


'''
    CREATE TABLE IF NOT EXISTS `user`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `username` VARCHAR(100) NOT NULL COMMENT '账号',
    `password` VARCHAR(500) NOT NULL COMMENT '密码',
    `type` VARCHAR(100) NOT NULL COMMENT '账号类型',
    `is_delete` TINYINT NOT NULL COMMENT '是否使用',
    `create_date` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '日期',
    `update_date` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新日期',
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
# # 循环
# for i in range(10):
#     #  创建新User对象:
#     user = User(username=f"{'liyinchi'+str(i)}",
#                         password='123456', type='1', is_delete=False)
#     # 
#     print(f"{user.username},{user.password},{user.type},{user.is_delete}")
#     # [添加到session]
#     session.add(user)
#     # user01=User(name='user01',uid=2.232,is_delete=True,gender="男",time=datetime(2020,10,31,17,38,30),longtext="xxxxxxxxxxx")
# #  [提交到session]
# session.commit()


# 精确查询
result1=session.query(User).filter(User.username=="liyinchi1").all()
for r in result1:
    print("r.username",r.username)
    print("r.id:",r.id)
print("精确查询======================")
session.commit()
    
# 模糊查询
result2=session.query(User).filter(User.username.like('%liyinchi%')).all()
for r in result2:
    print("r.username",r.username)
    print("r.id:",r.id)
print("模糊查询======================")
session.commit()


# 多值匹配（包含）
result3 =session.query(User).filter(User.username.in_(['liyinchi1','liyinchi2'])).all()
for r in result3:
    print("r.username",r.username)
    print("r.id:",r.id)
print("多值匹配======================")

# 多值不匹配（不包含）
result4 =session.query(User).filter(~User.username.in_(['liyinchi1','liyinchi2'])).all()
for r in result4:
    print("r.username",r.username)
    print("r.id:",r.id)
print("多值不匹配======================")


# is null
result5 =session.query(User).filter(User.username.is_(None)).all()
for r in result5:
    print("r.username",r.username)
    print("r.id:",r.id)
print("为空======================")

# is not null
result6 =session.query(User).filter(User.username.isnot(None)).all()
for r in result6:
    print("r.username",r.username)
    print("r.id:",r.id)
print("不为空======================")

# and
result7 =session.query(User).filter(User.username.like('%liyinchi%'),User.id>5).all()# 方法一
result7 =session.query(User).filter(and_(User.username.like('%liyinchi%'),User.id>5)).all()# 方法二
result7 =session.query(User).filter(User.username.like('%liyinchi%')).filter(User.id>5).all()# 方法三

for r in result7:
    print("r.username",r.username)
    print("r.id:",r.id)
print("多条件  且 and======================")

# or
result8 =session.query(User).filter(or_(User.username.like('%liyinchi%'),User.id>5)).all()# 方法二
for r in result8:
    print("r.username",r.username)
    print("r.id:",r.id)
print("或 or======================")

'''
func.count:统计行的数量。
func.avg:求平均值。
func.max:求最大值。
func.min:求最小值。
func.sum:求和。
func.distinct:求不重复的值。
func.
'''