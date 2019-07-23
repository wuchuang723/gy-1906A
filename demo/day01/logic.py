a = 20
if(a<10 and a>=5):
    print("小明只能买大前门")
if(a<25 and a>=10):
    print("小明能买红双喜或者大前门")
if(a>=25):
    print("小明能买玉溪、红双喜或者大前门")

m = 18
if(m>60):
    print("小明买老人票")
elif(m>=18):
    print("小明买成人票")
else:
    print("小明买未成年票")


for b in range(100):
    if (b % 2 == 1):
        print(b)

for c in range(50):
    print(2*c+1)


for d in range(9):
    for e in range(9):
        if(e<=d):
            print(d+1,"×",e+1,"=",(d+1) * (e+1),'\t',end='')
    print()

for k in range(1,100):
    for n in range(1,k+1):
        if(k*n>100):
            break
            print(k*n)






