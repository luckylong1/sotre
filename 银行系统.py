import random
message={}
#定义方法——用于添加用户
def useradd():
    user=input("请输入姓名")
    account=random.randint(10000000,99999999)
    password=input("请输入6位数字密码")
    bank='中国工商银行昌平支行'
    country=input("请输入国家")
    province=input("请输入省份")
    street=input("请输入街道")
    door=input("请输入门牌号")
    money=0
    num1=messageadd(user,account,password,bank,country,province,street,door,money)
    if num1 == 1:
        print("开户成功，以下是您的个人信息")
        info='''
                -------工商银行-------
                    1、账号：%s
                    2、姓名：%s
                    3、密码：******
                    4、银行：%s
                    5、国家：%s
                    6、省份：%s
                    7、街道：%s
                    8、门牌：%s
                    9、金额：%s
                ---------------------
        '''
        print(info % (account,user,bank,country,province,street,door,money))
    elif num1 == 2:
        print("您已开户，不能重复进行操作")
    elif num1 == 3:
        print("数据库满，不能添加")


def messageadd(user,account,password,bank,country,province,street,door,money):
    if user not in message:
        message[user]={
                "账号":account,
                "密码":password,
                "银行":bank,
                "国家":country,
                "省份":province,
                "街道":street,
                "门牌号":door,
                "金额":money
        }
        return 1
    elif user in message:
        return 2
    elif len(message)>=100:
        return 3

def conin():
    user=input("请输入姓名")
    jine=int(input("请输入存钱金额"))
    num1=conin1(user,jine)
    if num1 == True:
        print("存入成功！")
        print("当前余额为：",message[user]['金额'])
    else:
        print("没有这个用户")

def conin1(user,jine):
    if user in message:
        message[user]['金额'] += jine
        return True
    else:
        return False

def out():
   user=input("输入取款用户")
   password=input("取款密码")
   if user not in message:
       print("用户不存在")
   else:
       if password == message[user][password]:
           jine = int(input("取款金额"))
           if message[user]['金额'] < jine:
               print("您的金额不足")
           else:
               message[user]['金额'] -=jine
               print("取款成功！")
               print("您当前余额为：",message[user]['金额'])
       else:
           print("密码错误")
def inout():
    userout=input("请输入转出的用户")
    userin=input("请输入转入的用户")
    passwordout=input("请输入转出的密码")
    if userout and userin not in message:
        print("转出或转入用户不存在")
    else:
        if passwordout == message[userout]['密码']:
            jine=int(input("输入转出金额"))
            if message[userout]['金额'] < jine:
                print("钱不够，穷鬼")
            else:
                message[userout]['金额'] -= jine
                message[userin]['金额'] += jine
                print("转出后您的余额为：",message[userout]['金额'])
                print("您转入了：",message[userin]['金额'])
        else:
            print("转出用户密码不对")

def select():
    user=input("请输入用户名")
    password=input("请输入密码")
    if user not in message:
        print("用户不存在")
    else:
        if password == message[user]['密码']:
            print(message[user])
        else:
            print("密码错误")



while True:
    print('********************')
    print('*   中国工商银行     *')
    print('*   账户管理系统     *')
    print('*    V1.0          *')
    print('********************')
    print('                    ')
    print('*1.开户')
    print('*2.存钱')
    print('*3.取钱')
    print('*4.转账')
    print('*5.查询')
    print('*6.Bye！')
    print('********************')
    a=input("办理什么业务？")
    if a == "1":
        print("开户业务")
        useradd()
        print(message)
    elif a == "2":
        print("存钱业务")
        conin()
    elif a == "3":
        print("取款业务")
        out()
    elif a == "4":
        print("转账业务")
        inout()
    elif a == "5":
        print("查询业务")
        select()
    elif a == "6":
        print("退出系统")
        break




