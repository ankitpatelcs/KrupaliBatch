class A:
    def __init__(self):
        print('calling from class A')

class B(A):
    def __init__(self):
        super().__init__()
        print('calling from class B')
 
obj=B()
