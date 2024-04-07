# Understanding multiple inheritance

class A:
    def __init__(self):
        super().__init__()
        self.prop1 = 'prop1'
        self.name = 'Class A'


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = 'prop2'
        self.name = 'Class B'


# This is multiple inheritance 'class C(A,B)'
# You do not see this a lot in real world implementations as it can cause issues
# so stick to the inheritance_start file for inheritance
class C(A, B):
    def __init__(self):
        super().__init__()

    def show_props(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)


c = C()
print(C.__mro__)
c.show_props()
