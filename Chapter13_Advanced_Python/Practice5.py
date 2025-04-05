from functools import reduce

l = [45, 99, 146, 57, 108, 19, 2]

def max(a, b):
    if a > b:
        return a
    return b

maxNum = reduce(max, l)
print(maxNum)