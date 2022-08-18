class A:
    def __init__(self,num):
        self.num=num
    
    def __add__(self,n):
        return self.num + n.num

    

obj1=A(55)
obj2=A(33)
m=obj1+obj2
print(m)