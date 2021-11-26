import random
a=int(input("请输入第一条边"))
b=int(input("请输入第二条边"))
c=int(input("请输入第三条边"))

if a+b<=c or a+c<=b or b+c<=a or a-b>=c or a-c>=b or b-c>=a:
    print("不能构成三角形")
else:
    if a == b == c:
        print("等边三角形")
    elif a == b or a == c or b == c:
        print("等腰三角形")
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        print("直角三角形")
    else:
        print("普通三角形")


