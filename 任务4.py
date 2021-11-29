dict={"k1":"v1","k2":"v2","k3":"v3"}
# for x,y in dict.items:
#     print(x,y)

# dict["k4"]="v4"
# print(dict)
# dict.update({"翻斗花园":"胡图图"})
# print(dict)


# import random
# sum1=0
# sum2=0
# Friuts = {
# 	'苹果':12.3,  # 水果和单价
# 	'草莓':4.5,
#        '香蕉':6.3,
#        '葡萄':5.8,
#        '橘子':6.4,
#        '樱桃':15.8}
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#         'money': 0
#     },
#     '小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#         'money': 0
#     }
# }
#
# a=info.get('小明')
# xiaoming=a.get('fruits')
# print(xiaoming)
# b=info.get('小刚')
# xiaogang=b.get('fruits')
# print(xiaogang)
# for i in Friuts:
#     if i in xiaoming:
#         sum1 += Friuts[i] * xiaoming[i]
#     if i in xiaogang:
#         sum2 += Friuts[i] * xiaogang[i]
# info['小明']['money']=sum1
# info['小刚']['money']=sum2
# print(info)


# def p1(num):
#     a={}
#     for i in num:
#         if i not in a:
#             a[i]=1
#         else:
#             a[i] += 1
#     return a
# print(p1([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,55,55,55,5,55,555,55,5,5,555,6,7,8,6,7,8,9,9,9,9,]))
#


# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# holas=["姓名","年龄","性别","编号","任职公司","薪资","部门编号"]
# a=names[0]
# dict(zip(holas,a))


a=["刘备","56","男","106","IBM", 500 ,"50"]
b=["姓名","年龄","性别","编号","任职公司","薪资","部门编号"]
dict(zip(b,a))



