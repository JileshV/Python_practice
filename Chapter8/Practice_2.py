def add_natural(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return n + add_natural(n-1)


num = int(input("Enter a number upto which you want the addition of natural numbers: "))
print(f"The sum of natural numbers is {add_natural(num)}")