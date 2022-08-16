class Person:
    name=None

    #constructor
    def __init__(self,m):
        self.name=m
        
    # destructor
    def __del__(self):
        print('calling destructor')

p=Person('Smith')
print(p.name)
p2=Person('Rinkal')
print(p2.name)