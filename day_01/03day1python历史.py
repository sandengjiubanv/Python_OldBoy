#!/usr/bin/python
# -*- coding:utf-8 -*-
username = "wll"
password = 8888
count = 3
while count > 0:
    zh = input("请输入你的账号:")
    count -= 1
    if zh == username:
        mm = input("请输入你的密码:")
        if int(mm) == password:
            print("验证成功.正在登陆......")
            print('恭喜%s登陆成功!' % zh)
            break
        else:
            if count == 0:
                print("你的机会已经没了!")
                answer = input('再试试？Y or N')
                if answer == "Y":
                    count = 3
            print("密码错误,请重新输入")
            print("你还有"+str(count)+"次机会")
    else:
        if count == 0:
            print("你的机会已经没了!")
            answer = input('再试试？Y or N')
            if answer == "Y":
                count = 3
        print("请输入正确的用户名!")
        print("你还有%s次机会" % count)