class Employee:
    language = "Python" #Class attribute
    salary = 30000 #Class attribute

jilesh = Employee() #jilesh is an object/instance created
jilesh.name = "Jilesh Waghela" #jilesh.name is object/instance attribute
print(jilesh.name, jilesh.language, jilesh.salary)

ronak = Employee() #ronak is an object/instance create
ronak.name = "Ronak Waghela" #ronak.name is an object/instance attribute
print(ronak.name, ronak.salary, ronak.language)