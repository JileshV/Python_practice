n = int(input("Enter a number to get the factorial of the entered number: "))

factorial = 1
for i in range(1, n+1): #In for loop range does the increment of i and do not require separate i += 1
    factorial *= i

print(factorial)
