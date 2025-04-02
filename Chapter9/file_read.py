# File i/o

# f = open("file_1.txt")  #Opens a file
# data = f.read()  #reads content of a file
# print(data)
# f.close()  #Closed the opened file

# With Statement for opening and reading a file without explicitly adding cloe file

with open("file_1.txt") as f:
    print(f.read())