def hello(greeting, *args):
    if (len(args) == 0):
        print('%s!' % greeting)
    else:
        print('%s,%s!' % (greeting, ','.join(args)))  # join函数是用来表示用逗号将可变参数连接起来
hello('Hi')
hello('Hi', 'Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam')  # 以上三种形式都是直接传入variable parameter

names = ('Bart', 'Lisa')
hello('Hello', *names)  # 先组装成tuple，再传入，可变参数
