import random
uid='wsl'
umm='abc123'

a=0
for i in range(5):
    if a == 3:
        print("连续输错:3次，账户锁定！")
        break
    uid1 = input('请输入用户名：')
    umm1 = input('请输入密码：')
    if uid1 == uid and umm1 == umm:
        print("登录账号成功！")
        break
    else:
        a = a + 1
        print("已输错：",a,"次")

