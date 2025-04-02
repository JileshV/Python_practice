class Employee:
    language = "Python" #Class attribute
    salary = 30000 #Class attribute

    def getInfo(self):  #Instead of self, any name can be given
        print(f"The language is {self.language} & salary is {self.salary}")

    @staticmethod   #This can be used to eliminate self argument if there is no need of any class attribute inside a function
    def greet():
        print("Good Morning!")
        sum = 1 + 2

jilesh = Employee() #jilesh is an object/instance created
jilesh.language = "JavaScript"

jilesh.getInfo() #This line can be read as Employee.getInfo(jilesh)
