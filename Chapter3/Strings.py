a = 'Jilesh'
b = "Jilesh"
c = '''jilesh'''
d = "012345678"

print(a, b, c)

#String functions
strlength = len(a) #Length of a string
print(strlength)

print(b.endswith("esh")) #Checks if the string ends with 'esh' is True or not
print(b.startswith("ji")) #Checks if the string starts with 'ji' is True or not; Flase in this case is J is not capital
print(c.capitalize()) #Capitalizes only fisrt character of a string
print(a.count("J")) #Counts the number of times the given character presents in a string
print(a.find("s")) #Gets the index of the given character in the string
print(a.replace("J","N")) #Replaces the character J with character N

#Slicing a String
nameshort = a[0:3] #Slicing shortens the string from 0th index upto 2nd index character
print(nameshort)

nameshort = a[-3:-1] #Negative slicing
print(nameshort)

character = a[5] #Gets 4th index character
print(character)

nameskip = d[1:6:3] #Slices string from 1st index value till 5th and then skips values after every 2 indexes
print(nameskip)
nameskip = d[::2] #skips every 2nd index value
print(nameskip)
