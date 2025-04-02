try:
    a = int(input("Enter a number:"))
    print(a)

except Exception as e:   #With this, even user enters a string or any other thing, it will give error but still continue futher
    print(e)

except ValueError as v:
    print(v)

print("Thank you")