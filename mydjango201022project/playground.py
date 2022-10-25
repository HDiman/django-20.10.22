
class Foo:
    def __index__(self):
        return '123'

print(repr(int(Foo())))
