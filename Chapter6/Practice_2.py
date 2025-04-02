eng = int(input("Enter marks for subject English out of 100: "))
sci = int(input("Enter marks for subject Science out of 100: "))
mat = int(input("Enter marks for subject Maths out of 100: "))
geo = int(input("Enter marks for subject Geography out of 100: "))

average = (eng+sci+mat+geo)/4
if (eng>=33 and sci>=33 and mat>=33 and geo>=33):
    if (average>=40):
        print("Congratulations!! You have passed in all the subjects.")
    else:
        print("You have passed in all subjects but failed due to low average percentage.")
else:
    print("Sorry, you have failed in the exam")