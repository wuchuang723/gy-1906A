# for i in range(2,100):
#     n=2
#     for j in range(2,i+1):
#         if(i%n==0):
#             break
#         n=n+1
#         if(n==i):
#             print(i)


# a=0
# for i in [1,60,30,90,100,20,70,59,69,71,80,84]:
#     if(i < 60):
#         a=0
#     elif(i < 70 and i >=60):
#         a=1
#     elif(i < 80 and i >= 70):
#         a=2
#     else:
#         a=3
#     if(a == 0):
#             print(i,"不及格")
#     if(a == 1):
#             print(i,"及格")
#     if(a == 2):
#             print(i,"良好")
#     if(a == 3):
#             print(i,"优秀")

# a = 0
# for i in [90,100,81,84]:
#     if(i < 80):
#         a=1
# if(a == 1):
#     print("不全优秀")
# else:
#     print("全是优秀")

# a = "01010010001110001001001010101010010101"
# m = 0   # m代表多少个0
# n = 0   # n代表多少个1
# for i in a:
#     if(i == '0'):
#         m = m+1
#     else:
#         n = n+1
# print("有",m,"个0,",n,'个1')

# i = 1
# s = 0
# while(i<=100):
#     s=s+i
#     i=i+1
# print(s)

# s = 0
# for i in range(1,101):
#     s = s + i
# print(s)

i=1
s=1
while(i<=10):
    s=s*i
    i=i+1
    print(s)    