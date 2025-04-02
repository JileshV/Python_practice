# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(input("Enter a number for multiplication table: "))

table = [i*num for i in range(1, 11)]   #No need of list1, we can use range(1, 11)
print(table)

i = 0
for n in table:
    print(f"{num} X {i+1} = {table[i]}")
    i += 1