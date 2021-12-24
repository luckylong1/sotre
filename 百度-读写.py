'''
有一个百度的日志文本文件，要求将IP地址截取下来，并计算出现了多少次
要求：以字典的方式展现出来
log文件地址：D:\测试项目\PythonProject\day14【文件读写】\baidu_x_system.log
'''

#写法1
import time
# f = open(file = "baidu_x_system.log",mode = "r+",encoding="utf-8")
# num = {}
# while True:
#     f1 = f.readlines()
#     ip = ""
#     for i in f1:
#         ip = i.split(' ',-1)
#         if ip[0] in num:
#             num[ip[0]] += 1
#         else:
#             num[ip[0]] = 1
#     print(num)
#     time.sleep(30)


#写法2
from collections import Counter
f = open(file = "baidu_x_system.log",mode = "r+",encoding="utf-8")
while True:
    f1 = f.readlines()
    ip = []
    for i in f1:
        a = i.split(' ',-1)
        ip.append(a[0])
    print(Counter(ip))
    time.sleep(3)
