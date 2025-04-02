a = 46

def fun():
    global a
    a = 10
    print(f"The value of a in function is {a}")

fun()
print(a)