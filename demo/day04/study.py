def st(h1,h2):
    return "{} kill {} game over".format(h1,h2)
print(st('ice','fire'))

def sf(h1,h2,h3):
    return "{m1} kill {m2} game over {m3}".format(m1=h3,m2=h1,m3=h2)
print(sf('ice','fire','vn'))

# 不定向参数
# *args用于多个数据，**kwargs用于字典
def sum(*args):
    print(args)
    s = 0
    for i in args:
        s += i
    return s
def s(**kwargs):
    print(kwargs)

print(sum(1,2,3,4,5))
s(name = 'ice',sex = 'man')