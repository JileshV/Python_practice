class Employee:
    # def __init__(self, salary, increment):
    salary = 50000
    increment = 13
    
    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) - 1) * 100

e1 = Employee()
# print(e1.salaryAfterIncrement)
e1.salaryAfterIncrement = 56500
print(e1.increment)