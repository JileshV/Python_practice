class Calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")

    def sq_root(self):
        print(f"The suqare root of {self.n} is {self.n**0.5}")

    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")

num = int(input("Enter a number: "))
cal = Calculator(num)

a = input("Enter s for Square / r for Sq root / c for cube: ")

if (a == 's'):
    cal.square()
elif (a == 'r'):
    cal.sq_root()
elif (a == 'c'):
    cal.cube()
else:
    print("Error!")