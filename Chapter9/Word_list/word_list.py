c = ["donkey", "shitty", "hated", "cunning"]

for i in range (0, len(c)):
    with open("Word_list\words.txt") as f:
        text = f.read()
    text_new = text.replace(c[i], "*"*len(c[i]))
    with open("Word_list\words.txt", "w") as f:
        f.write(text_new)
