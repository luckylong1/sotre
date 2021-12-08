import random
from DBUtils import update
from DBUtils import select
#定义方法——用于添加用户
def useradd():
    username=input("请输入姓名")
    userid=random.randint(10000000,99999999)
    password=input("请输入6位数字密码")
    bankname='中国工商银行昌平支行'
    country=input("请输入国家")
    province=input("请输入省份")
    street=input("请输入街道")
    door=input("请输入门牌号")
    money=0
    num1=messageadd(username,userid,password,bankname,country,province,street,door,money)
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
        print(info % (userid,username,bankname,country,province,street,door,money))
    elif num1 == 2:
        print("您已开户，不能重复进行操作")
    elif num1 == 3:
        print("数据库满，不能添加")


def messageadd(username,userid,password,bankname,country,province,street,door,money):
    sql = "select * from user where username = %s"
    param=[username]
    data = select(sql,param,"all")
    sql2 = "select count(*) from user"
    param2 = []
    data2 = select(sql2,param2,"all")
    if len(data) == 0:
        sql1 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param1 = [userid,username,password,bankname,country,province,street,door,money]
        update(sql1,param1)
        return 1
    elif len(data) > 0:
        return 2
    elif data2 >= 100:
        return 3

def conin():
    username=input("请输入姓名")
    jine=int(input("请输入存钱金额"))
    num1=conin1(username,jine)
    if num1 == True:
        print("存入成功！")
    else:
        print("没有这个用户")

def conin1(username,jine):
    if jine < 0:
        print("存款不得小于0")
    else:
        sql3 = "select * from user where username = %s"
        param3 = [username]
        data3 = select(sql3,param3,"all")
        if len(data3) > 0:
            sql4 = "update user set money = money + %s"
            param4 = jine
            update(sql4,param4)
            return True
        else:
            return False
#
def out():
   username=input("输入取款用户")
   password=input("取款密码")
   sql4 = "select password,money from user where username = %s"
   param4 = [username]
   data4 = select(sql4,param4,"all")
   print(data4)
   if len(data4) == 0:
       print("用户不存在")
   else:
       if password == data4[0][0]:
           jine = int(input("取款金额"))
           if data4[0][1] < jine:
               print("您的金额不足")
           else:
               sql5 = "update user set money = money - %s where username = %s"
               param5 = [jine,username]
               update(sql5,param5)
               print("取款成功！")
       else:
           print("密码错误")
def inout():
    userout=input("请输入转出的用户")
    userin=input("请输入转入的用户")
    passwordout=input("请输入转出的密码")
    sql5 = "select * from user where username = %s"
    param5 = [userout]
    data5 = select(sql5,param5,"all")
    sql6 = "select * from user where username = %s"
    param6 = [userin]
    data6 = select(sql6,param6,"all")
    if len(data5) == 0 or len(data6) == 0:
        print("转出或转入用户不存在")
    else:
        if passwordout == data5[0][2]:
            jine=int(input("输入转出金额"))
            if data5[0][8] < jine:
                print("钱不够，穷鬼")
            else:
                sql7 = "update user set money = money - %s where username = %s"
                param7 = [jine,userout]
                update(sql7,param7)
                sql8 = "update user set money = money + %s where username = %s"
                param8 = [jine,userin]
                update(sql8,param8)
                print("转账成功！")
        else:
            print("转出用户密码不对")

def select1():
    username=input("请输入用户名")
    password=input("请输入密码")
    sql9 = "select * from user where username = %s"
    param9 = [username]
    data9 = select(sql9,param9,"all")
    if len(data9) == 0:
        print("用户不存在")
    else:
        if password == data9[0][2]:
            print(data9[0])
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
        select1()
    elif a == "6":
        print("退出系统")
        break




