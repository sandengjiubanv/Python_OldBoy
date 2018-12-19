#!/usr/bin/python
# -*- coding:utf-8 -*-
# 作业二：编写登陆接口
# 输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后锁定
#
# username = "wll"
# userpassword = 8888
# count = 0
# all_count = 3
# while count < 3:
#     input_username = input("请输入你的用户名：")
#     input_password = input("请输入你的密码：")
#     if username == str(input_username) and userpassword == int(input_password):
#         print("Success login!!!")
#         break
#     else:
#         all_count = all_count - 1
#         print('''
# 用户名或者密码错误 !!!
# 你输入的用户名为：%s
# 你输入的密码为：%s
# 你还有 %s 次机会！！！
#               '''
#               %(input_username, input_password, all_count))
#         count += 1
# else:
#     print("hehe")

username = "wll"
userpassword = 8888
count = 3
while count > 0:
    input_username = input("请输入你的用户名：")
    if username == str(input_username):
        input_password = input("请输入你的密码：")
        if userpassword == input_password:
                print("欢迎 %s 登入系统!!!" % input_username)
                break
        else:
            count -= 1
            print(count)
            print('''
                密码错误 !!!
                你输入的用户名为：%s
                你输入的密码为：%s
                你还有 %s 次机会！！！
                  '''
                  %(input_username, input_password, count))
            if count == 0:
                print("你的机会已用完，你是否想继续？")
                answer = input("请输入 [Y] or [N]～")
                if str(answer) == "Y":
                    count = 3
                    print(count)
    else:
        count -= 1
        print("你输入的用户名不存在,你还有%s次机会"%count)
        continue
else:
    print("你的机会已用完,再见～")


