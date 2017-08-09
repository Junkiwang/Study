import math


def s(r):
    s = math.pi * (r**2)
    return s
R = float(input('请输入圆的半径：'))
s(R)
print('圆的面积为：%.2f\n' % s(R))

import math


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad urand type')
    if not isinstance(b, (int, float)):
        raise TypeError('bad urand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad urand type')
    if a == 0:
        x = -c / b
        return x
    if (b**2 - 4 * a * c) < 0:
        return('系数不合理，此方程无解')
    else:
        x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        return(x1, x2)
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
d = quadratic(a, b, c)
print(d)
