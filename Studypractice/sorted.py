L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()
L1 = sorted(L, key=by_name)
print(L1)


def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print(L2)


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f())
    return fs
f1, f2, f3 = count()
print(f1, f2, f3)


# fix:


def count():
    fs = []

    def f(n):
        def g():
            return n * n
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())


def count():
    fs = []

    def f(n):
        return lambda: n * n
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())


import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25\n')

now()  # 调用函数


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@logger('DEBUG')
def today():
    print('2015-3-25\n')


today()  # 调用函数


print(today.__name__, '\n')


def fuck(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call: %s()' % func.__name__)
        a = func(*args, **kw)
        print('end call: %s()' % func.__name__)
        return a
    return wrapper


@fuck
def rizhi(x):
    return x + 1
print(rizhi(1))
