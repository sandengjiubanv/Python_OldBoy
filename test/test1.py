# # Author:wll
# # http://www.cnblogs.com/jin-xin/articles/7459977.html
#
# # 1、使用while循环输入1 23456 8910
# i = 0
# while i < 11:
#     i += 1
#     if i == 7:
#         print('')
#     else:
#         print(i)
# # 2、求1-100的所有数的和
# j = 1
# g = 0
# while j < 101:
#     j += 1
#     g = j + g
# else:
#     print(g)
# # 3、输出1-100内的所有奇数
# j = 1
# g = 0
# while j < 101:
#     j += 2
#     g = j + g
# else:
#     print(g)
# # 4、输出1-100内的所有偶数
# j = 2
# g = 0
# while j < 101:
#     j += 2
#     g = j + g
# else:
#     print(g)
# # 5、求1-2+3-4+5 ... +99的所有数的和
# j = 1
# g = 0
# while j < 100:
#     if j % 2 == 0:
#         g = g - j
#     else:
#         g = g + j
#     j+=1
# print(g)
# # else:
# #     print(g)
#
# # 6、用户登陆(三次机会重试)
# user = "wll"
# password = "wll123"
# count = 0
# while count < 3:
#     user_input = input("please input username: ")
#     print(type(user_input))
#     user_passowrd = input("plese input userpassword: ")
#     print(type(user_passowrd))
#     if user == user_input and password == user_passowrd:
#         print("welcome come")
#         break
#     else:
#         print("error username or password ~~~")
#     count += 1
#
#
#
# # 补充
# while True:     # 效率低
#     pass
#
# while 1:        # 效率高
#     pass
#
#
# # 简洁判断
# s = input("balabala: ")
# if s:
#     print("您输入的是空: ")
# else:
#     pass
#
#
#

# # -*- coding: utf-8 -*-
# words = input("请输入单词：")
# words_length = len(int(words))
# # print(words_length)
# print("字符长度为：", str(words_length))
#
# words_count = words.split(' ')
# print(words_count)
# print(len(words_count))
# print("单词个数为：", str(len(words_count)))
#





s = 'dwaoidoiawdoiohoq'

# for i in s:
#     print(i)


# index = 0
# while 1:
#     print(s[index])
#     index += 1
#     if index == len(s):
#         break


content = input("请输入加数 + 被加数: ").strip()


w = content.find("+")
print(w)

print(content[0:w])

# print(content.lstrip("+"))


