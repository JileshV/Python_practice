num = int(input("Enter a number to get specified number of star rows: "))

for i in range(1, num+1):
    print(" "*(num-i), end="") #end expression prevents a new line while running in loop
    print("*"*(2*i-1), end="")
    print("")


#   *
#  ***
# ***** for n = 3