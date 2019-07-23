# 创建
a = []
# 列表最后新增单个值
a.append(1)
a.append("djalkdjlaj")
a.append("95")
print(a)
# 合并
b = [1,3,5,6]
# 使用extend方法合并两个列表（生成一个新的列表）
print(a+b)
# 使用extend方法合并两个列表（在原来列表的末尾添加一个列表中的元素）
a.extend(b)
print(a)

# 删
# 根据下标删除某个元素
a.pop(0)
print(a)
# 默认删除列表中最后一个元素
a.pop()
print(a)
# 清空一个列表
# a = []
# print(a)
# a.clear()
# print(a)

# 改
# 根据下标修改某个元素的值
a[0],a[1] = 0,1
print(a)

# 查
# 根据下标查询某个元素
print(a[0])
print(a[1])
# 遍历（借助循环）
for i in a:
    print(i)

# 截取
# 截取部分数据
print(a[1:3])
# 倒叙
print(a[::-1])
# a.reverse()
# print(a)
# 隔一个取一个
print(a[::2])

# 求列表的长度
print(len(a))