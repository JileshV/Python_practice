l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)

def even(n):
    if (n%2 == 0):
        return True
    return False

evenList = filter(even, l)
print(list(evenList))