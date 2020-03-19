# import doctest
# import time
# import _thread
# import unittest
# from datetime import date
# # import mysql.connector
#
# #date test
# def dateTest():
#     print date.today()
#
# # mysql test
# conn = mysql.connector.connect(
#     host="192.168.18.118",
#     user="ytxroot",
#     passwd="ytxmysqlpass",
#     database="iris"
# )
#
# c=conn.cursor()
# c.execute("SHOW TABLES")
# # for i in c:
#     # print i
#
# sql="insert into krisTest (`name`,`url`) values(%s,%s)"
# param=("kris","www.baidu.cpm")
# params=[
#     ("a","1"),
#     ("b","2"),
#     ("c","3"),
#     ("d","4"),
# ]
# # c.execute("CREATE TABLE krisTest (name VARCHAR(255), url VARCHAR(255))")
# # c.execute(sql,param)
# # c.executemany(sql,params)
# # conn.commit()
# # print c.lastrowid
#
# querySql="select * from krisTest"
# # c.execute(querySql)
# # all=c.fetchall()
# # for i in all:
# #     print (i)
#
# # print "s"
#
# # c.execute("select * from krisTest where id =4")
# # for i in c.fetchall():
#     # print i
#
# # c.execute("select * from krisTest")
# # for i in c.fetchone():
#     # print i
#
#
#
#
#
