def main():
    for n in primers():
        if n < 100:
            print(n)
        else:
            break


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return (lambda x: x % n > 0)


def primers():
    yield 2
    it = _odd_iter()  # it一开始是一个以3开头的奇数数列，通过第26行逐渐筛选出不是素数的数变成素数数列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
if __name__ == '__main__':
    main()


def is_odd(n):
    return n % 2 == 1
L = range(100)
print(list(filter(is_odd, L)))


def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))


def _no_divisible(n):
    return lambda x: x % n > 0
foo = _no_divisible(4)
print(foo)
print(foo(11))
print(foo(12))


def is_palindrome(n):
    if str(n)[0:] == str(n)[::-1]:
        return True
output = filter(is_palindrome, range(1, 1000))
print(list(output))


def s_palindrome(n):
    x = len(str(n))
    for i in range(0, x):
        if str(n)[i] == str(n)[x - i - 1]:
            # 此处一个数字中比较出两个数对了一次就返回了，有剩下的不相同的数就比较不了了
            return True
put = filter(s_palindrome, range(1, 105))
print(list(put))


def palin(n):
    x = len(str(n))
    for i in range(0, x):
        if str(n)[i] != str(n)[x - i - 1]:
            return False
    return True
a = filter(palin, range(1, 105))
print(list(a))
