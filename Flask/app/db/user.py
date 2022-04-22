#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# https://docs.sqlalchemy.org/en/14/orm/quickstart.html
# SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Date, Time, DECIMAL, Text, create_engine
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
# 循环
for i in range(10):
    #  创建新User对象:
    user = User(username=f"user{'liyinchi'+str(i)}",
                        password='123456', type='1', is_delete=False)
    # 
    print(user)
    # [添加到session]
    session.add(user)
    # user01=User(name='user01',uid=2.232,is_delete=True,gender="男",time=datetime(2020,10,31,17,38,30),longtext="xxxxxxxxxxx")
#  [提交到session]
session.commit()

