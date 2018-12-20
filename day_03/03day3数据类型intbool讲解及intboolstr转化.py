i = 100
print(i.bit_length())
'''
                  bit_length
1     0000 0001       1
2     0000 0010       2
3     0000 0011       2
'''


# bool  True False

# int ----> str
i = 1
s = str(i)

# str ---> int
s = '123'
i = int(s)
print("i",i)

# int ----->bool  只要是0 ----》False  非0就是True
i = 3
b = bool(i)
print(b)
# bool----> int
# True   1
# False  0
i = 0
b = bool(i)
print(b)

'''
ps:
while True:
    pass
while 1: 效率高
    pass
'''

# str --->bool

# s = "" -----> False
# 非空字符串都是True
# s = "0" -----> True

s1 = "0"
i = bool(s1)
print("s1", i)

s2 = ""
i = bool(s2)
print("s2", i)

s3 = " "
i = bool(s3)
print("s3", i)

# s
# if s:
#     print('你输入的为空，请重新输入')
# else:
#     pass

