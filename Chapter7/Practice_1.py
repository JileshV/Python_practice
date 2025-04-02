num = int(input("Enter a number to get a multiplication table for the same: "))

for i in range (1, 11):
    print(f"{num} X {i} = {num*i}")
    i +=1
