# type()类
def fn(self, name='world'):
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
print('call h.hello')
h.hello()
print('type(Hello) =', type(Hello))
print('type(h) =', type(h))

# metaclass()元类


class ListMetaclass(type):

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class Mylist(list, metaclass=ListMetaclass):
    pass
# list没有add()的方法的,只有append()
L = Mylist()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)


'Simple ORM using metaclass'


class Field(object):

    def __init__(self, name, cloumn_type):
        self.name = name
        self.cloumn_type = cloumn_type

    def __str__(self):
        return'<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            # 这里其实是想删除attrs中的所有属性，而python3不允许遍历过程中删除正在遍历的字典中的元素,会报错，所以用mappings遍历
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (
            self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
