marks = {
    "Ronak" : 99,
    "Vinay" : 68,
    "Sagar" : 75,
    "Ram" : 56
}

print(marks.items()) #Lists the whole dictionary

print(marks.keys()) #Lists values of all keys

print(marks.values()) #Lists values of all values

marks.update({"Vinay" : 61, "Jilesh" : 85}) #Adds/updates Keys, values
print(marks)

print(marks.get("Jilesh")) #Displays value of the specified key

# marks.clear() #Empties a dictionary
# print(marks)

marks2 = marks.fromkeys(marks, 5) #Creates a new dictionary and assgins keys from mentioned dictionary and new specifcied value
print(marks2)

removed_marks = marks.pop("Sagar", "ERROR") #Removes a specified key's key-value
print(removed_marks)
print(marks)

removed_item = marks.popitem() #Removes last inserted key-value
print(removed_item)
print(marks)