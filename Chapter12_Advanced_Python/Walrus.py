# ':=' is a walrus operator, used to directly assign & check with operator in any conditional statement

if (n := len([2, 5, 9, 4, 1]) > 3):
    print(f"The list is too long,{n} elements present, expected less than 3")