class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
s = Student('Michael')
print(s)


class Chain(object):

    def __init__(self, path=''):    # 默认路径参数path为空
        self._path = path

    def __getattr__(self, path):
        print('call __getattr__(%s)' % path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, param):
        print('call __call__(%s)' % param)
        return Chain('%s/%s' % (self._path, param))

    __repr__ = __str__
print(Chain().status.user.timeline.list)
print(Chain().user('Bob').repos)