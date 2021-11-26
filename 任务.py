import random
num1=int(input("请输入第1个数"))
num2=int(input("请输入第2个数"))
num3=int(input("请输入第3个数"))
num4=int(input("请输入第4个数"))
num5=int(input("请输入第5个数"))
num6=int(input("请输入第6个数"))
num7=int(input("请输入第7个数"))
num8=int(input("请输入第8个数"))
num9=int(input("请输入第9个数"))
num10=int(input("请输入第10个数"))
ran=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]
he=sum(ran)
print(he)

sum1=0
for i in range(len(ran)):
    sum1=sum1+ran[i]
    if i == 9:
        print(sum1)

print(max(ran))
print(min(ran))
print(sum(ran)/len(ran))

a=random.randint(50,150)
print(a)

