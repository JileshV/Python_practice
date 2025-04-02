a = int(input("Enter a number to get it divided: "))
b = int(input("Enter another number to divide the above number: "))

if (b == 0):
    raise ZeroDivisionError("The answer is INFINITY! Please enter a valid divisor.")

print(f"{a}/{b} = {a/b}")