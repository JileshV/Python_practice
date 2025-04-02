def tables(n):
    for n in range (1, n+1):
        for i in range (1, 11):
            c = f"{n} X {i} = {n*i}"
            # print(c)
            if (i < 2):
                with open(f"Tables\Table_{n}.txt", "w") as f:
                    f.write(c+"\n")
            if (i >= 2):
                with open(f"Tables\Table_{n}.txt", "a") as f:
                    f.write(c+"\n")


n = int(input("Enter number upto which want to get tables of: "))
tables(n)