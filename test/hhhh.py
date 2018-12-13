# -*- coding: utf-8 -*-
import os
path1 = input("请输入目录(默认当前目录): ")
f = open('tmp.txt', 'w')
if path1 == "":
    print("默认使用当前目录")
    path1 = os.getcwd()
    os.chdir(path1)
    print("当前目录为 : ", os.getcwd())
    list1 = os.listdir()
    print("当前目录下有文件夹：")
    for i in list1:
        path_file = os.getcwd() + "/" + str(i)
        # print(path_file)
        if os.path.isdir(path_file):
            print(i)
            f.write(i + '\n')
else:
    os.chdir(path1)
    print("当前目录为 : ", os.getcwd())
    list1 = os.listdir()
    print("当前目录下有文件夹：")
    for i in list1:
        path_file = os.getcwd() + "/" + str(i)
        # print(path_file)
        if os.path.isdir(path_file):
            print(i)
            f.write(i + '\n')
f.close()

# -*- coding: utf-8 -*-

# import os,sys
#
# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         print(root) #当前目录路径
#         print(dirs) #当前路径下所有子目录
#         print(files) #当前路径下所有非目录子文件
#
# path = "/Users/erlong/OneDrive/PycharmProjects/s9/test/"

#
# # -*- coding: utf-8 -*-
# import os, sys
# # reload(sys)
# # sys.setdefaultencoding('utf-8')
# def all_path(dirname):
#     print(os.walk(dirname))
#     for maindir, subdir, file_name_list in os.walk(dirname):
#         for filename in file_name_list:
#             print(filename)
# path = "/Users/erlong/OneDrive/PycharmProjects/s9/test/"
#
# # path="F:/项目文档/项目结算交付件/03&04&05/v1.0/审计材料/16、数据提取脚本执行/方案&脚本"
# # path="F:/项目文档/项目结算交付件/03&04&05/v1.0/审计材料16、数据提取脚本执行/tmp/"
# # all_path(path.decode('utf-8'))
#


