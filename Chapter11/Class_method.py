class Number:
    a = 1
    @classmethod    #Class method enables the function to use class attribute and not object/instance attribute
    def show(cls):
        print(f"The value of class attribute is {cls.a}")

obj = Number()
obj.a = 20

obj.show()