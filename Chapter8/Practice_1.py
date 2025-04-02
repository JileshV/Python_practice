def greatest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))

print(f"The greates number of all three is {greatest(n1, n2, n3)}")