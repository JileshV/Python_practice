dict1 = {
    "ped" : "tree",
    "kursi" : "chair",
    "chai" : "tea",
    "kalam" : "pen"
}

user_key = input("Enter a word in hindi to translate: ")
print(dict1.get(user_key))