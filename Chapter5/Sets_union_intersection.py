s1 = {1, 5, 8}
s2 = {61, 5, 12, 1}
s3 = {1, 61}

print(s1.union(s2)) #Adds both sets with no repeating values

print(s1.intersection(s2)) #Displays only common values from both sets

print(s3.issubset(s1)) #Checking if s3 is a subset of s1 which is false
print(s3.issubset(s2)) #Checking if s3 is a subset of s2 which is true

print(s2.issuperset(s3)) #s2 is a superset of s3