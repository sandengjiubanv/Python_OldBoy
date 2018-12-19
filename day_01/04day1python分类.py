#!/usr/bin/python
# -*- coding:utf-8 -*-
username = "yangxiaoer"
password = "123456"
i = 3
while i > 0:
    zh = input("请输入你的账号:")
    i -= 1
    if zh == username:
        mm = input("请输入你的密码:")
        if mm == password:
            print("验证成功.正在登陆......")
            print('''恭喜你登陆成功!
            欢迎用户进入
            用户名 :%s
            密码   :%s
            '''%(zh,mm))
            break
        else:
            if i == 0:
                print("你的机会已经没了!game over 下次见!")
                answer = input('再试试？Y or N')
                if answer == 'Y':
                    i = 3
            print("密码错误,请重新输入")
            print("你还有"+str(i)+"次机会")
    else:
        print("请输入正确的用户名!")
        if i == 0:
            print("你的机会已经没了!")
            answer = input('再试试？Y or N')
            if answer == 'Y':
                i = 3
        print("你还有" + str(i) + "次机会")
else:
    print('你TM要不要脸')