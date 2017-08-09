L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)
print(L[0:8])
print(list(range(100))[0:50])
print()

M = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('M[0:3] =', M[0:3])
print('M[:3] =', M[:3])
print('M[1:3] =', M[1:3])
print('M[-2:] =', M[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])
print('R[::-1] = ', R[::-1])
print()

N = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('N[::3] =', N[::3])
print('N[::] =', N[::])
print()

name = ['Adam', 'Alex', 'Amy', 'Bob', 'Boom', 'Candy', 'Chris',
        'David', 'Jason', 'Jasonstatham', 'Junki', 'Bill']

i_name = input('please input name:').title()  # title()函数把字符串转换为标题格式，即首字母大写
wname = []
for n in name:
    print(n)
    if n[0:len(i_name)] == i_name:
        wname.append(n)
if len(wname) != 0:
    print('Do you want to find %s ?' % (wname))
else:
    print('%s is not find' % (i_name))
print()
s = 'strabcdefgst'
print(s.strip('str'))   # 去掉字符串中的首部和尾部带'str'的
print(s.lstrip('str'))  # 去掉字符串中的首部带'str'的
print(s.rstrip('str'))  # 去掉字符串中的尾部带'str'的

for a, b, c in [('arry', 'dfd', 'gdae')]:
    print(a, b, c)
print()
alist = [0, True, 1.5, 'list']
atuple = (0, 1, 1.2, False, 'tuple')
aset = {0, 1.1, True, 'set'}
for first, *middle, last in (alist, atuple, aset):
    print(first)
    print(middle)
    print(last)
