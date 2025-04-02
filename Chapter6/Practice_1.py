a = float(input("Enter 1st number:"))
b = float(input("Enter 2nd number:"))
c = float(input("Enter 3rd number:"))
d = float(input("Enter 4th number:"))

if (a>b and a>c and a>d):
    print(f"a, {a} is the greatest number")

if (b>a and b>c and b>d):
    print(f"b, {b} is the greatest number")

if (c>b and c>a and c>d):
    print(f"c, {c} is the greatest number")

if (d>b and d>c and d>a):
    print(f"d, {d} is the greatest number")
