class Abc:
    @staticmethod
    def a():
        print('static method')

    def b(self):
        print('Instance Method')

    @classmethod
    def c(Abc):
        print('class method')

j=Abc()
j.a()
j.b()
j.c()