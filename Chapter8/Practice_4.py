def rem(l, word):
    for item in l:
        l.remove(word)
        return l

def strip(l, word):
    n = []
    for item in l:
        if not item == word:
            n.append(item.strip(word))
    return n

l1 = ["Jilesh", "Rohan", "Ronak", "an"]

print(rem(l1, "an"))
print(strip(l1, "an"))