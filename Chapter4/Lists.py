
#LISTS ARE MUTABLE

list = ["Orange", "Banana", "Ronak", 25, "Rohan", 254.48]
print(list[2])

list[2] = "Jilesh" #Changes "Ronak" to "Jilesh"
print(list[2])

print(list[1:4])

list.append("Jagdish") #Adds "Jagdish" at the end of the list
print(list)

numbers = [21, 6, 88, 67, 104, 46, 2, 49]
# numbers.sort() #Arranges a list in ascending order
# print(numbers)

# numbers.reverse() #Arranges a list in descending order
# print(numbers)

numbers.insert(4, 119) #Inserts 119 at index 4
print(numbers)

numbers.pop(1) #Deletes value at index 1
print(numbers)

print(numbers.pop(2)) #Displays the value from list at index 2
print(numbers)

int = numbers.pop(2) #Can remove a value from list at index 2 and assign it to a variable
print(int)
print(numbers)

numbers.remove(2) #Removes '2' value from the list
print(numbers) 