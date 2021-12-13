# class geli:
#     __brand = ""
#     __price = 0
#
#     def start(self):
#         print("空调开机了..")
#
#
#     def setBrand(self,brand):
#         self.__brand = brand
#
#     def Getbrand(self):
#         return self.__brand
#
#     def setPrice(self,price):
#         if price > 5000 or price < 0:
#             print("价格不公道！")
#         else:
#             self.__price = price
#
#     def Getprice(self):
#         return self.__price
#
#     def end(self,endtime):
#         print("空调在",endtime,"分钟后关机")
#
#     def brand(self):
#         print("空调品牌是",self.__brand,"的")
#
#     def price(self):
#         print("空调价格是",self.__price)
#
# a = geli()
#
# a.start()
# a.setBrand("格力")
# a.Getbrand()
# a.setPrice(4500)
# a.Getprice()
#
# a.brand()
# a.price()
# a.end(10)

# class student1:
#     __name = ""
#     __age = 0
#
#     def setAge(self,age):
#         self.__age = age
#
#     def Getage(self):
#         return self.__age
#
#     def setName(self,name):
#         self.__name = name
#
#     def Getname(self):
#         return self.__name
#
#     def ziwojieshao(self):
#         print("大家好，我叫",self.__name,"，今年",self.__age,"岁了！")
#
#     def bijiao(self,Age):
#         if self.__age > Age:
#             print("我比同桌大",self.__age-Age,"岁")
#         elif self.__age < Age:
#             print("我比同桌小", Age - self.__age,"岁")
#         else:
#             print("我俩一样大！")
# a = student1()
# a.setAge(15)
# a.Getage()
# a.setName("小明")
# a.Getname()
# a.ziwojieshao()
# a.bijiao(20)

#
# class people:
#     __name = ""
#     __sex = ""
#     __age = 0
#     __huafei = 0
#     __pinpai = ""
#     __dianchi = 0
#     __pingmu = 0
#     __jifen = 0
#     def setName(self,name):
#         self.__name = name
#     def Getname(self):
#         return self.__name
#     def setSex(self,sex):
#         self.__sex = sex
#     def Getsex(self):
#         return self.__sex
#     def setAge(self,age):
#         self.__age = age
#     def Getage(self):
#         return self.__age
#     def setHuafei(self,huafei):
#         print("还有",huafei,"话费")
#         self.__huafei = huafei
#     def Gethuafei(self):
#         return self.__huafei
#     def setPinpai(self,pinpai):
#         print("手机是",pinpai,"的")
#         self.__pinpai = pinpai
#     def Getpinpai(self):
#         return self.__pinpai
#     def setDianchi(self,dianchi):
#         print("电池是",dianchi,"毫安的")
#         self.__dianchi = dianchi
#     def Getdianchi(self):
#         return self.__dianchi
#     def setPingmu(self,pingmu):
#         print("屏幕是",pingmu,"寸的")
#         self.__pingmu = pingmu
#     def Getpingmu(self):
#         return self.__pingmu
#     def setJifen(self,jifen):
#         self.__jifen = jifen
#     def Getjifen(self):
#         return self.__jifen
#
#     def faduanxin(self,neirong):
#         print("短信发送成功，内容为：",neirong)
#
#     def dadianhua(self,number,time):
#         if len(number) < 11 or len(number) > 11:
#             print("号码是空号")
#         else:
#             if self.__huafei<1:
#                 print("余额不足")
#             else:
#                 if time < 10:
#                     self.__huafei -= 1*time
#                     self.__jifen += 15*time
#                     print("当前话费为：",self.__huafei,"积分为",self.__jifen)
#                 elif time >= 10 and time <= 20:
#                     self.__huafei -= 0.8*time
#                     self.__jifen += 39*time
#                     print("当前话费为：", self.__huafei, "积分为", self.__jifen)
#                 else:
#                     self.__huafei -= 0.65 * time
#                     self.__jifen += 48 * time
#                     print("当前话费为：", self.__huafei, "积分为", self.__jifen)
#
# a = people()
#
# a.setAge(22)
# a.setSex("男")
# a.Getsex()
# a.Getage()
# a.setName("詹姆斯")
# a.Getname()
# a.setJifen(10)
# a.Getjifen()
# a.setPingmu(8)
# a.setDianchi(5000)
# a.Getdianchi()
# a.setHuafei(100)
# a.Gethuafei()
# a.setPinpai("苹果")
# a.Getpinpai()
#
# a.faduanxin("今天天气还不错")
#
# a.dadianhua("12012012012",10)

# class student:
#     number = 0
#     name = ""
#     age = 0
#     sex = ""
#     hige = 0
#     wight = 0
#     score = 0
#     home_street = ""
#     phone_number = 0
#
#     def learn(self,hour):
#         print(self.name,"已经学习了",hour,"个小时")
#     def playGame(self,Gname):
#         print(self.name,"正在玩",Gname)
#     def pycham(self,hang):
#         print(self.name,"写了",hang,"行代码")
#     def sum(self):
#         a=int(input("请输入第一个数"))
#         b=int(input("请输入第二个数"))
#         print("和为",a+b)
# g=student()
# g.number = 1001
# g.name = "王思聪"
# g.age = 22
# g.sex = "男"
# g.hige = 181
# g.wight = 130
# g.score = 740
# g.home_street = "深圳湾1号"
# g.phone_number = 110
#
# g.learn(3)
# g.playGame("吃鸡")
# g.pycham(500)
# g.sum()

# class car:
#     xinghao = ""
#     chelun = 0
#     yanse = ""
#     zhongliang = 0
#     youxiang =0
#     def run(self,juli):
#         print("车最多可以跑",juli,"公里")
#     def price(self):
#         print("品牌:",self.xinghao," 颜色:",self.yanse," 油箱:",self.youxiang,"升")
# a = car()
# a.xinghao = "法拉利"
# a.chelun = 4
# a.yanse = "红"
# a.zhongliang = 1
# a.youxiang = 50
#
# a.run(600)
# a.price()


# class bjb:
#     xh = ""
#     dj = 0
#     ys = ""
#     zl = 0
#     cpu = ""
#     nc = 0
#     yp = 0
#     def playGame(self,name):
#         print("正在打",name)
#
#     def bangong(self):
#         print("正在办公")
#
# a = bjb()
# a.playGame("LOL")
# a.bangong()


# class monkey:
#     leibie = ""
#     xingbie = ""
#     yanse = ""
#     tizhong = 0
#     def fire(self,cl):
#         print(self.leibie,"正在用",cl,"生火")
# a = monkey()
# a.leibie="金丝猴"
# a.fire("红木")







