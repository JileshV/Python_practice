name_list = ["Rohan", "Sagar", "Vikas", "Vinay"]

input_name = input("Enter your name: ")

name = input_name.capitalize() #Capitalise first letter if user enters lower case name

if(name in name_list):
    print(f"Your name {name} is present in the list!")
else:
    print(f"Your name {name} is NOT present in the list!")