#! /usr/bin/env python
# -*- coding: utf-8 -*-


'''
按照扑克牌的规则，现在有6张牌，只要5张
黑桃（S）红桃（H）方块（D）梅花（C）
牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
'''
# a = '''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''
# #字符串的替换
# a = a.replace("''",'"')
# #字符串截取
# a = a[2:-2]
#
# print(a)
#
# #字符串的切片方法
#
# b = a.split('" , "')
#
# print(b)
#
# #key 唯一；并且存一对数据
# #key存牌的大小，value存key出现的次数
# #{'1':3,"10":1,"7":2}
# d = {}
# for i in b:
#     c = i[1:]
#     if(c in d):
#         d[c] += 1
#     else:
#         d[c] = 1
# print(d)
# m = []
# for key in d:
#     m.append(d[key])
# print(m)
# if 3 in m and 2 in m:
#     print("该数据满足3带2牌型")
# else:
#     print("该数据不满足3带2牌型")



# def是方法定义的关键字，juge_3_2是方法名，可以自定义，不能以数字开头，()参数列表:
def juge_3_2(a):
    # 第一步：统一符号  对字符串的处理，用replace（）
    # a = input()
    a = a.replace("''",'"')
    # print(a)
    # 第二步：去掉中括号 字符串截取  [::]
    a = a[2:-2]
    # print(a)
    # 第三步：变成list  字符串切片  .split（） 新建一个list变量
    b = a.split('" , "')
    # print(b)
    # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取

    # 第五步：统计相同的数字个数  用字典去统计
    d_dict = {}
    for i in b:
        c = i[1:]
        if(c not in d_dict):
            d_dict[c] = 1
        else:
            d_dict[c] += 1
    # print(d_dict)
    # 第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
    v1 = 0 # 如果key对应的数值有3的 v1 = 1，如果没有则为0
    v2 = 0 # 如果key对应的数值有2的 v2 = 1，如果没有则为0
    for key in d_dict:
        if(d_dict[key] == 3):
            v1 = 1
        if(d_dict[key] == 2):
            v2 = 1
    if(v1 == 1 and v2 == 1):
        print("该数据满足3带2牌型")
    else:
        print("该数据不满足3带2牌型")
# for i in range(3):
#     juge_3_2()

# open python提供的一个内置函数：作用就是打开一个文件，参数一：文件路径，参数二：文件的打开模式r只读，w可写入，a可读可写入
# with open() as f 类似于 f = open(),他可以在with的代码执行出问题的时候，做一些资源释放的工作
with open ("D:\\softwareDate\\pycharm\\wuch_1906A\\demo\\day04\\cards.txt","r") as f:
    # 读文件，readlines()作用就是把文件中所有的内容按行读取出来，存到一个list中，read()把整个文件的内容读取出来，存都一个字符串中
    lines = f.readlines()
    # for循环遍历这个列表
    for line in lines:
        # 去掉每一行末尾的换行符
        line = line.replace('\n','')
        print(line)
        # 调用一个方法，判断牌型是否是3带2
        juge_3_2(line)

