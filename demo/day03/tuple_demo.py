# 列表和元组的区别
# 1、元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = (50,)
print(tup1)

# 2、元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del(tup)
print(tup)
# "After deleting tup : "
# print(tup)