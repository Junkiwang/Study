s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generation return value:', e.value)
        break


def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]


n = 0
for x in triangles():
    print(x)
    n = n + 1
    if n == 10:
        break


# 杨辉三角的特点是新一行的每个数字等于其两肩的数字之和。
# 将已有行进行补0错位[1,1]-->[0,1,1]和[1,1,0]然后相加即可得到新一行。
# 这是在数学上使用技巧，可以简化代码。


def triangle(n):
    l, lnext = [1], [1]
    for i in range(n):
        yield l  # print(l)
        l, lnext = l + [0], [0] + lnext
        l = lnext = [l[t] + lnext[t] for t in range(len(l))]
    return 'done'


for i in triangle(10):
    print(i)


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break
# yield L给出第一行[1]，然后对L进行第一轮重新赋值，
# range(len(L)-1)使得从0开始到len(L)-1,第一轮从0到0，所以中间的L[i]+L[i+1]不起作用，进而使得L变成[1，1]
# 重复上述过程yield L,核心想法：只关注每行除掉首尾“1”的其他非“1”项
