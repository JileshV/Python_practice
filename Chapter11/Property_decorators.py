class Number:
    a = 1
    @classmethod    #Class method enables the function to use class attribute and not object/instance attribute
    def show(cls):
        print(f"The value of class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

obj = Number()
obj.a = 20

obj.show()

obj.name = "Jilesh Waghela"
print(obj.fname, obj.lname)