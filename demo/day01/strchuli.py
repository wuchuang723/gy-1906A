# a = "看不见你的笑我怎么睡得着,你的身影这么近我却抱不到，你要离开，我知道很简单，" \
#     "你说依赖是我们的阻碍，就算放开，但能不能别没收我的爱，当作我最后才明白" \
#     "牧笛横吹黄酒小菜又几碟" \
#     "无关风月我提序等你回，悬臂一绝那岸边浪千叠" \
#     "情字何解怎罗比都不对，而我独缺你一生的了解" \
#     "我看着你的脸，轻刷着和弦，情人节卡片手写的永远，初恋是整遍手写的从前" \
#     "突然好想你，你会在哪里，过得快乐或委屈，突然好想你突然锋利的回忆"
# print(a[3:6])
# print(a[-6:])

# 按照扑克牌的规则，现在有6张牌，只要5张
# 黑桃（S）红桃（H）方块（D）梅花（C）
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
a = '''[''D1'',''H1'',''H10'',''H7'',''S1'',''S7'']'''
# a = a[1:-1]
# a_li = a.split(",")
# print(a_li)
# for i in a_li:
#     a = i[3:-2]
#     print(a)

# a = a.replace("''","'")
# print(a)

a = '1,2,3,4,5,6,7,8,9'
# 截取
# 截取单个字符
print(a[2])
# 截取其中一段
print(a[2:7])
# 字符串倒叙排序
print(a[::-1])
# 隔一个字符截取一个字符
print(a[::2])

# 切片
# 以逗号把字符串切割成n个子串，并存入一个列表中
print(a.split(','))

# 替换
# 把字符串中的4替换成10
print(a.replace('4','10'))
# 把字符串中的4替换成10，只替换一次
print(a.replace('4','10',1))

# 查找find和rfind
sentence="This is a apple"
print(sentence.find("a"))
print(sentence.rfind("a"))
# 运行结果：
# 8
# 10

a = "https://www.runoob.com/python/python-install.html"
b = a.split('://')[1]
print(a.split('://')[0])
print(a.split('://')[1])
ym = b[:b.find('/')]
uri = b[b.find('/'):]
print(ym)
print(uri)