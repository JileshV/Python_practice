def star_pattern(n):
    if n == 0:
        return 0
    print("*"*n, end="")
    print("")
    star_pattern(n-1)

num = int(input("Enter a number to get reverse * pattern: "))
star_pattern(num)