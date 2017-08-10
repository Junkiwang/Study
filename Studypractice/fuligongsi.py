L = input('依次输入用“/”间隔每年利率：')
P = float(input('输入买入价格：'))
F = float(input('输入到期价值：'))
L = L.split('/')
L = list(map(float, L))
print(L)


def f(r):
    n = len(L)
    N = F / (1 + r) ** n
    sum = 0
    for i in range(n):
        sum += L[i] / (1 + r) ** (i + 1)
    M = sum
    y = P - M - N
    return y


a = 0
b = 1
fa = f(a)
fb = f(b)
c = (a + b) / 2
fc = f(c)
d = 0
while abs(fc) >= 0.0001:
    if fa * fc >= 0:
        fa = fc
        a = c
    else:
        fb = fc
        b = c
    c = (a + b) / 2
    fc = f(c)
    d += 1
print(d, c, f(c))

print('到期收益率为：%s%%' % (c * 100))
