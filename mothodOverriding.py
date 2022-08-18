class Employee:
    def display(self):
        print('calling from Employee')

class Payroll(Employee):
    def display(self):
        print('calling from Payroll')

p=Payroll()
p.display()