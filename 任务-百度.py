import xlrd

a=xlrd.open_workbook(filename=r"百度合作单位-人员管理-二期.xls",encoding_override=True)
b=a.sheet_by_index(0)
# sump=b.nrows
# print(sump)

number=b.col_values(5)
dianxin=0
liantong=0
yidong=0

# for i in number:
#     if i.startswith("14" or "17"):
#          dianxin += 1
#     elif i.startswith("13"):
#             yidong += 1
#     elif i.startswith("15"):
#             liantong += 1
# print("电信：",dianxin,
#       "联通：",liantong,
#       "移动：",yidong)

# sex1=0
# sex2=0
# sex=b.col_values(8)
# for i in sex:
#     if i == '男':
#         sex1 += 1
#     elif i == '女':
#         sex2 += 1
# print("男性:",sex1)
# print("女性:",sex2)

# old=0
# c=b.col_values(7)
# for i in c:
#     if i > 45:
#         old += 1
# print(old)

# d=b.col_values(11)
# s_sal=0
# for i in d:
#     if i > 8000 or i < 3000:
#         s_sal += 1
# print(s_sal)

# e=b.col_values(9)
# ssum=0
# for i in e:
#     if i.startswith("黑龙江" or "北京" or "福建" or "四川"):
#         ssum += 1
# print(ssum)

list1=b.col_values(13)
s=0
for i in list1:
    if i.endswith("传媒有限公司"):
        s += 1
print(s)

