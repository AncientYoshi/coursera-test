# Example 1
class A:
    a = 1


class B:
    b = 2


class C(A, B):
    pass


c = C()
print(c.a, c.b)


class A:
    a = 1


class B(A):
    a = 2


class C(B):
    pass


c = C()
print(c.a)
