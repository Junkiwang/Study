print('fish is'.startswith('fis', 0, 3))  # 0是'fis'的起始位置，3是'fis'的字节长度


class UpperattrMetaclass(type):

    def __new__(cls, name, bases, attrs):
        upper_attrs = ((name, value)
                       for name, value in attrs.items() if not name.startswith('__'))
        uppercase_attrs = dict((name.upper(), value)
                               for name, value in upper_attrs)
        return type.__new__(cls, name, bases, uppercase_attrs)


class Foo(object, metaclass=UpperattrMetaclass): #python3指定的元类创建方式，放在括号里
    bar = 'bip'
class Goo(Foo):
	faq = 'bop'
print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
f = Foo()
print(f.BAR)
print(hasattr(Goo, 'faq'))
print(hasattr(Goo, 'FAQ'))
g = Goo()
print(g.FAQ)