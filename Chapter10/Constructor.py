class Employee:
    language = "Python" #Class attribute
    salary = 30000 #Class attribute

    def __init__(self, name, salary, language):     #It is called dunder method which does not required to be called unlike other functions in a class
        self.name = name
        self.salary = salary
        self.language = language
        print("This is a dunder method & called automatically")

    def getInfo(self):  #Instead of self, any name can be given
        print(f"The language is {self.language} & salary is {self.salary}")

# jilesh = Employee()
# jilesh.name = "Jilesh"
# print(jilesh.name, jilesh.salary)

ronak = Employee("Ronak", 100000, "React")
print(ronak.name, ronak.salary, ronak.language)
