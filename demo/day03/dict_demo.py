# 增
# 创建
a = {}
# 字典中新增一对数据
a["姓名"],a["定位"] = "Vn","ADC"
print(a)
# 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
a["姓名"] = "金克斯"
print(a)
# key是不可改变的，元组(1,2,3,4)可以作为key，但是(1，[3])不可以作为一个key
a[(1,2)] = 3
print(a)

# 删----pop参数只能为key
# a.pop("定位")
# del a["姓名"]
# print(a)
# # 清空字典
# a.clear()
# print(a)

# 改
a["姓名"] = "金克斯"
print(a)

# 查
# 根据key查看value
print(a["姓名"])

# 字典中的数据是无序排列的

# 遍历字典（借助循环）
for key in a:
    print(a[key])

# # 字典合并
# c = {"name":"Ming"}
# d = {"sex":"boy"}
# c.update(d)
# print(c)
# # 两个字典合并，生成一个新字典
# print(dict(c,**d))
#
# #成员判断（key）
# if("sex" in c):
#     print("存在字典中")
# else:
#     print("不存在字典中")
#
# # 获取字典长度
# print(len(c))


