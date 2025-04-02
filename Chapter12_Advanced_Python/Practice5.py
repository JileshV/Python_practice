num = int(input("Enter a number for multiplication table: "))

table = [i*num for i in range(1, 11)]   #No need of list1, we can use range(1, 11)
print(table)

i = 0
for n in table:
    c = (f"{num} X {i+1} = {table[i]}")
    # if (i < 1):
    #     with open("Tables.txt", "w") as f:
    #         f.write(c+"\n")
    # else:
    with open("Tables.txt", "a") as f:
        f.write(c+"\n")
    print(c)
    i += 1