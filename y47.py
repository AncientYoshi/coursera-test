class A:
    def a(self):
        return 1


class B(A):
    pass


class C(B):
    pass


c = C()
print(c.a())
