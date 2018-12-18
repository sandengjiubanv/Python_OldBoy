#!/usr/bin/python
# -*- coding:utf-8 -*-
# 作业三：多级菜单
# 三级菜单
# 可依次选择进入各子菜单
# 所需新知识点：列表、字典


# a = {'11', {'12'}, '22', '33', '44', '55', '66'}
# b = ['1', '2', '3', '4', '5', '6']
# print(a[0, 0])


# while True:
#     input_info = input("Please input info: ")

# i = 1
# sum = 0
# while i < 100:
#     if i == 88:
#         i += 1
#         continue
#     if i%2 != 0:
#         sum += i
#     else:
#         sum -= i
#     i += 1
# print(sum)
sum = 0
i = 0
j = -1
while i < 99:
    i += 1
    j = -1
    if i == 88:
        continue
    else:
        sum += sum + i*j
print(sum)

a = 12&127
print(a)




