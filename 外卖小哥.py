'''
外卖小哥
店铺位置：昌平，解放路，外卖店和客户地址
送达地址：昌平，翻斗花园101室
一层层判断，如果shop的客户地址等于client的地址，就把外卖添加进去，增加跑腿费
最后定义函数，调用函数就可以了
'''
import random
dict_shop={"昌平":{"解放路":{"煎饼店":"煎饼","麻辣烫店":"麻辣烫","客户地址":"101室","跑腿费":30}}}
dict_client={"昌平":{"翻斗花园":"101室"}}
money=20
while True:
    for i in dict_shop:
        a=input("请输入大区")
        if a in dict_shop:
            a1=input("请输入街道")
            if a1 in dict_shop[a]:
                    print(dict_shop[a][a1])
                    a2 = input("请选择店铺")
                    if a2 in dict_shop[a][a1]:
                        print("已取餐，请稍后")
                        b = input("请输入送往大区")
                        if b in dict_client:
                            b1 = input("请输入小区")
                            if dict_client[b][b1] == dict_shop[a][a1]['客户地址']:
                                money = money + dict_shop[a][a1]['跑腿费']
                                print("已送达，请支付", money, "元")
                                break

