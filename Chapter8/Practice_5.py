def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter a number to get its multiplication table: "))
table(n)