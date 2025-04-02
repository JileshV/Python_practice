user_name = input("Enter a username with atleast 10 characters: ")

if (len(user_name) < 10):
    print("The username entered does not have 10 characters.")
else:
    print("The username is valid")