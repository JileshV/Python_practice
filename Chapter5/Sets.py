#Set
#Elements/values cannot be repeated in a set
#Sets are is unordered

s1 = {1, 5, 8}

s2 = set() #Creates s2 as an empty set
print(type(s2))

s1.add(50) #Adds a value into the Set
print(s1)

print(len(s1)) #Length of a set

s1.remove(5) #Removes a specified value from the set
print(s1)

# s1.pop() #Removes random value from a set
# print(s1)

# s1.clear()
# print(s1)