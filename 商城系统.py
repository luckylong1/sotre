'''
    Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10个辣条优惠券（0.3），20个威猛先生优惠券（0.9），免单一张优惠券，先整体打折8后在单独打折，
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
'''

import random
store=[
    ["辣条",5],
    ["鸡蛋",10],
    ["锅",200],
    ["榴莲",300],
    ["威猛先生",20],
    ["费列罗",400],
    ["运动鞋",150],
    ["羽绒服",500],
    ["酱油",10],
    ["小冰箱",50],
]
money=1000
mycar=[]
luck=random.randint(1,4)
if luck == 1:
    print("恭喜，10张辣条3折劵")
elif luck ==2:
    print("恭喜，20张威猛9折劵")
elif luck ==3:
    print("恭喜您，免单啦！")
else:
    print("恭喜您，本单8折！")
num0=0
num4=0

while True:
        for i in enumerate(store):  # 列举出商品名称
            print(i)
        buy = input("请输入物品序号")
        if buy.isdigit():
            buy = int(buy)
            if buy > 9 or buy < 0:
                print("没有该物品")
            else:
                if money < store[buy][1]:
                    print("你买不起，穷鬼！")
                else:
                    if buy == 0 and num0 <= 10 and luck == 1:
                        mycar.append(store[buy])
                        money = money - store[buy][1] * 0.3
                        num0=num0+1
                        print("所选商品已加入购物车，当前余额为：", money)
                        print("您的辣条优惠券已用",num0,"张")
                    elif buy == 4 and num4 <= 20 and luck == 2:
                        mycar.append(store[buy])
                        money = money - store[buy][1] * 0.9
                        num4 = num4 + 1
                        print("所选商品已加入购物车，当前余额为：", money)
                        print("您的辣条优惠券已用", num4, "张")
                    elif luck == 3:
                        mycar.append(store[buy])
                        print("所选商品已加入购物车，当前余额为：",money)
                    elif luck == 4:
                        mycar.append(store[buy])
                        money = money - store[buy][1] * 0.8
                        print("所选商品已加入购物车，当前余额为：",money)
                        print("已为您使用8折优惠！")
                    else:
                        mycar.append(store[buy])
                        money = money - store[buy][1]
                        print("所选商品已加入购物车，当前余额为：",money)
        elif buy == 'q' or buy == 'Q':
            print("感谢光临，下面是您的小票")
            for k in enumerate(mycar):
                print(k)
            break
        else:
            print("输入错误")

