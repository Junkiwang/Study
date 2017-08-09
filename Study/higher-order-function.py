f = abs
print(f)
print(f(-19))


def l(name):
    L = []
    for x in name:
        x = x.lower()
        x = x.title()
        L.append(x)
    return L


L1 = ['adam', 'LISA', 'barT']
print(l(L1), '\n')


def normalize(name):
    name = name.title()
    return name


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2, '\n')

from functools import reduce


def prod(L):
    def f(x, y):
        return x * y

    return reduce(f, L)


print('3*5*7*9 =', prod([3, 5, 7, 9]))

from functools import reduce


def str2float(s):
    L = list(s)
    n = 0
    for x in L:
        n += 1
        if x == '.':
            break  # print(n)
    a = L[0:(n - 1)]
    b = L[n:]
    c = a + b  # print(c)，用split函数切片更方便

    def f(x, y):
        return 10 * x + y

    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                '6': 6, '7': 7, '8': 8, '9': 9}[c]

    m = reduce(f, map(char2num, c))
    n = m / (10 ** (len(L) - n))
    return n


print('str2float(\'1.\') =', str2float('1.'))

from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)


print(str2int('0'))
print(str2int('123000'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}


def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, nums, 0.0)


print(str2float('0'))
print(str2float('123.456'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))


def normalize(name):
    a = len(name)
    if ord(name[0:1]) > 96:
        name = chr(ord(name[0:1]) - 32) + name[1:]
    n = 1
    if ord(name[n:(n + 1)]) > 96:
        name = name[0:n] + name[n:(n + 1)] + name[(n + 1):]
    else:
        while ord(name[n:(n + 1)]) > 64 and ord(name[n:(n + 1)]) < 91:
            name = name[0:n] + chr(ord(name[n:(n + 1)]) + 32) + name[(n + 1):]
            n += 1
            if n == (a - 1):
                name = name[0:n] + chr(ord(name[n:]) + 32)
                break
    return name


L1 = ['Adam', 'LisA', 'bART']
L2 = list(map(normalize, L1))
print(L2)
