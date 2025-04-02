num = int(input("Enter a number to make * box pattern: "))

for i in range(1, num+1):
    if(i == 1 or i == num):
        print("*"*num, end="")
    else:
        print("*", end="")
        print(" "*(num-2), end="")
        print("*", end="")
    print("")



# ***
# * *
# *** for n= 3

# ****
# *  *
# *  *
# **** for n = 4