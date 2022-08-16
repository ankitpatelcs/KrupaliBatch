class A:
    def a(self):
        print('calling from class A')

class B:
    def a(self):
        print('calling from class B')
    
class C(B,A):
    def c(self):
        self.a()
        #self.b()
        print('calling from class C')

obj=C()
obj.c()