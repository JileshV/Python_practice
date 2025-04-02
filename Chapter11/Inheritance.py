class Employee():       #BASE CLASS
    company = "Infosys"
    name = "Jilesh"
    salary = 50000
    # def __init__(self, name, salary):
    #     self.name = name
    #     self.salary = salary
    
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}.")

class Programmer(Employee):     #INHERITED CLASS
    company = "Infosys India"
    language = "Python"
    # def __init__(self, language):
    #     self.language = language
    #     super.__intit()      #SUPER METHOD RUNS INIT CONSTRUCTOR FROM PARENT CLASS AS WELL
    
    def showLang(self):
        print(f"The name of the programmer is {self.name} in company, {self.company} and he is profecient in {self.language}.")

a = Employee()
a = Programmer()
a.show()
a.showLang()
a.show()