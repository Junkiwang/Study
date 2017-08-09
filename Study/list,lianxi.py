from collections import Iterable, Iterator


def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}
print('iter key:', d)
for k in d.keys():
    print('key:', k)

print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C'], 1):  # 1表示从1开始编号，没有则从0开始
    print(i, value)

print('iter[(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

print([x * x for x in range(1, 13)])  # 列表生成式
print([m + n + c for m in 'abc' for n in 'abc' for c in 'abc'])

import os
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'WOrld', 17, 'ApPle', None]
print([s.lower() for s in L if isinstance(s, str)])  # lower()函数是对字符串大写字母转换成小写

# L = ['Hello', 'World', 17, 'Apple', None]
# L1 = []
# for n in L:
#    if isinstance(n, str):
#        L1.append(n)
# print([s.lower() for s in L1])

a = [x * x for x in range(1, 10)]
for b in a:
    print(b)
