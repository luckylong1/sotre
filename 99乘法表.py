
# i=1
# while i < 10:
#     j=1
#     while j <= i:
#         print(i," * ",j," = ",i*j,end=' ')
#         j=j+1
#     print(" ")
#     i = i + 1

for a in range(9,0,-1):
    for b in range(1,a+1,1):
        print(b,' * ',a,' = ',a*b,end=' ')
    print(' ')
