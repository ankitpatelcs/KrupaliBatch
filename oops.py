#declaration
class Employee:
    id=None #static/class attributr
    name=None
    def getdata(self):
        self.id=int(input('Enter ID: '))
        self.name=input('Enter Name: ')

    def showdata(self):
        print(f'ID: {self.id}')
        print(f'Name: {self.name}')

# object of class Employee
e=Employee()
e.getdata()
e.showdata()