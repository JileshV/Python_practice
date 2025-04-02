f = open("file_1.txt")

# lines = f.readlines()   #Reads the file and creates list of lines
# print(lines)
# print(type(lines))

line1 = f.readline()   #Reads a single line each time this function is run
print(line1)
print(type(line1))

line2 = f.readline()
print(line2)
print(type(line2))

line3 = f.readline()
print(line3)
print(type(line3))

f.close()