
with open("Donkey_practice\Donkey.txt") as f:
    text = f.read()
    print(text)

c = "donkey"
text_new = text.replace(c, "######")

with open("Donkey_practice\Donkey.txt", "w") as f:
    f.write(text_new)
