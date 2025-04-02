class Employee:
    language = "Python" #Class attribute
    salary = 30000 #Class attribute

jilesh = Employee() #jilesh is an object/instance created
jilesh.language = "JavaScript"
print(jilesh.language, jilesh.salary)

# Specified instance value will overwrite the attribute value
# as it is explicitly assigned to particular object/class "jilesh"
