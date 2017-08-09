L = [1, 2, 3, 4, 5]
l = []
for n in L:
    l.append(n)
print(l)
a = {'id': 12345, 'name': 'Mchiael',
     'email': '350187552@qq.com', 'password': '350188wjq'}
d = {'id': 12345, 'name': 'Mchiael',
     'email': '350187552@qq.com', 'password': '350188wjq'}
# 想清除a,python3不允许遍历过程中删除正在遍历的字典中的元素,会报错，所以用d遍历，删除a中的元素。
for m in d.keys():
    a.pop(m)
print(a)
print(d)
for i in range(1, 4):
    print(i)
import math
print(math.pi)
print(math.cos(math.pi / 3))  # python的三角函数使用的是弧度制，必须先用角度转换成弧度才行
print(math.sin((math.pi / 180) * 90))
