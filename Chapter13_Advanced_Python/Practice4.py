l = [5, 6, 55, 48, 95, 25, 47, 33]

def divFive(n):
    if (n%5 == 0):
        return True
    return False

divL = filter(divFive, l)
print(list(divL))
