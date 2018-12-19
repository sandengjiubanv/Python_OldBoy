#!/usr/bin/python
# -*- coding:utf-8 -*-
username = "wll"
userpassword = 8888
count = 3
while count > 0:
    ningzi = input("输入用户名：")
    if ningzi == username:
        mima = input("请输入你的尼玛")
        if mima == userpassword:
            print("欢迎登陆%s" %username)
            break
    else:
        count -= 1
        print("你输入的用户名不正确，你还有%s次机会" % count)





