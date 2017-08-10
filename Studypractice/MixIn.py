class Fish(object):
    pass


class DanshuiyuMixIn(Fish):
    pass


class HaishuiyuMixIn(Fish):
    pass


class CaoshixingyuMixIn(Fish):
    pass


class RoushixingyuMixIn(Fish):
    pass


class MamalMixIn(Fish):
    pass


class Caoyu(DanshuiyuMixIn, CaoshixingyuMixIn):
    pass


class Heiyu(DanshuiyuMixIn, RoushixingyuMixIn):
    pass


class Zhenzhudiao(HaishuiyuMixIn, CaoshixingyuMixIn):
    pass


class Jingyu(HaishuiyuMixIn, RoushixingyuMixIn, MamalMixIn):
    pass


a = Zhenzhudiao()
print(isinstance(a, Fish))
print(isinstance(a, DanshuiyuMixIn))
print(isinstance(a, HaishuiyuMixIn))
print(isinstance(a, CaoshixingyuMixIn))
print(isinstance(a, RoushixingyuMixIn), '\n')
b = Jingyu()
print(isinstance(b, Fish))
print(isinstance(b, DanshuiyuMixIn))
print(isinstance(b, HaishuiyuMixIn))
print(isinstance(b, CaoshixingyuMixIn))
print(isinstance(b, RoushixingyuMixIn))
print(isinstance(b, MamalMixIn))
