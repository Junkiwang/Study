L = input('输入用“/”间隔的均流数据:')
L = L.split('/')
L = list(map(float, L))
print(L)
sum = 0
for n in L:
    sum += n
average_value = sum / len(L)
l = []
for m in L:
    difference_value = abs(m - average_value)
    l.append(difference_value)
n = l.index(max(l))
result = (max(l) / average_value) * 100
print('平均值为：%s' % average_value)
print('极值为：%s' % L[n])
print('均流不平衡度为：%s%%' % result)
