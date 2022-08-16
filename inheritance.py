
from tempfile import gettempdir


class Employee:
    id=None
    name=None

    def GetEmp(self):
        self.id=1
        self.name='Parth'

    def ShowEmp(self):
        print(f'ID: {self.id}')
        print(f'Name: {self.name}')

class Payroll(Employee):
    salary=None

    def GetData(self):
        self.GetEmp()
        self.salary=25000

    def ShowData(self):
        self.ShowEmp()
        print(f'Salary: {self.salary}')

p=Payroll()
p.GetData()
p.ShowData()