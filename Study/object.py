'a test module'
__author__ = 'Junki Wang'
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments')

if __name__ == '__main__':
    test()

#
sd1 = {'name': 'ShaoWei', 'score': 100}
sd2 = {'name': 'ZuoBing', 'score': 100}


def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

print_score(sd1)
print_score(sd2)

#


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %d' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score > 60:
            return 'B'
        else:
            return 'C'
std1 = Student('Junki', 100)
print(std1.name)
print(std1.score)
std1.print_score()
print(std1.get_grade())

#


class student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def ger_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
bart = student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())
print('DO NOT use bart._student__name:', bart._student__name)

#


class Animal(object):

    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
b = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('b is Animal?', isinstance(b, Animal))
print('b is Dog?', isinstance(b, Dog))
print('b is Cat?', isinstance(b, Cat))

run_twice(c)

# type()

print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))

import types

print('type(\'abc\')==str?', type('abc') == str)


class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x'))  # 有属性‘x’吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性‘y’吗？
setattr(obj, 'y', 19)  # 设置一个属性‘y’
print('hasattr(obj, \'y\') =', hasattr(obj, 'y'))  # 有属性‘y’吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y'))  # 获取属性‘y’
print('obj.y =', obj.y)  # 获取属性‘y’

print('getattr(obj, \'z\') =', getattr(
    obj, 'z', 404))  # 获取属性‘z’，如果不存在，返回默认值404

f = getattr(obj, 'power')  # 获取属性’power‘
print(f)
print(f())