def factorial(n): #Defining a function
    if n==0 or n==1:
        return 1
    return n * factorial(n-1) #Recursion is calling a function within itself

num = int(input("Enter a number to get its factorial: "))

ret = factorial(num)
print(f"The factorial of {num} is {ret}")