# def math(a,b):
#     if(b == 0):
#         print('加:', a,'+', b,'=',a + b,'\t','减:', a,'-',b,'=',a - b,'\t',
#           '乘:', a,'x', b,'=',a * b,'\t','除:', a,'÷',b,'无意义')
#     else:
#         print('加:', a,'+', b,'=',a + b,'\t','减:', a,'-',b,'=',a - b,'\t',
#           '乘:', a,'x', b,'=',a * b,'\t','除:', a,'÷',b,'=',a / b)
# with open ("D:\\softwareDate\\pycharm\\wuch_1906A\\demo\\day04\\cards.txt","r") as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.replace('\n', '')
#         line_li = line.split(",")
#         math(int(line_li[0]),int(line_li[1]))


def sum(m,n):
    s = m + n
    print(m,"+",n,"=",s)
    return s

def sub(m,n):
    s = m - n
    print(m,"-",n,"=",s)

def mul(m,n):
    s = m * n
    print(m,"×",n,"=",s)

def div(m,n):
    if(n == 0):
        print(m,"÷",n,"无意义")
    else:
        s = m / n
        print(m,"÷",n,"=",s)

sum(9,3)
sum(sum(9,3),5)



