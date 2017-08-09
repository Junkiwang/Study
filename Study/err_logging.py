import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')  # 打印出错误后还能继续执行后面的语句


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')


bar()
