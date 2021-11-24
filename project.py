# 需求：
# 1、设定一个随机数
# 2、设定一个键盘输入
# 3、循环判断
# 任务：输入的大于随机数则打印“猜大了”，小于打印“猜小了”
# ，等于打印“猜对了”并退出循环；
# 起始金额5000，猜对给300，错了扣100，错15次退出循环

import random
a=0
jine=5000
while 1:
    i=input("猜猜是什么数？")
    i=int(i)
    Ran=random.randint(1,10)
    if i == Ran:
        print("猜对咯，奖励300块！")
        jine=jine+300
        break
    elif i > Ran:
        print("猜大咯，要扣100块！")
        jine=jine-100
        a=a+1
    elif i < Ran:
        print("猜小啦，再来一次！")
        jine=jine-100
        a=a+1
    if a >= 15:
        print("运气不佳，猜错15次了！")
        break