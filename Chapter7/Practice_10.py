n = int(input("Enter a number to get reverse multiplication table: "))

for i in range (0, 10):
    print(f"{n} X {10-i} = {n*(10-i)}")


# 3 X 10 = 30
# 3 X 9 = 27
# 3 X 8 = 24
# 3 X 7 = 21
# ...