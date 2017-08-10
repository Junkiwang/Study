def print_scores(**kw):
    print('      Name Score')  # 前面空6个空格加上自己单词4个字符刚好10个字符，用于打印时格式对齐。
    print('------------------')
    # 10s表示打印时有10个字符空位从最后往前铺，把前面空出来，适合于名字长的。%s和%d之间的空格，表示名字和数字用空格间隔一下。
    for name, score in kw.items():
        print('%10s %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)  # 关键字参数直接传入

data = {'Adam Lee': 99, 'Lisa S': 88, 'F.Bart': 77}
# Keyword parameter 组装成dict，再传入
print_scores(**data)
print()


def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=20)

print_info('Lisa', gender='female', city='Shanghai', age=18)


def person(name, age, *args, city='beijing', job):
    print(name, age, args, city, job)
person('michael', 19, job='cooker')
