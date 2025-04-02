with open("file_1.txt") as f:
    text = f.read()
    count = text.count("twinkle")
    if count >= 1:
        print(f"Yes, the file contains the word Twinkle {count} times.")
    else:
        print("The file does not contain the word Twinkle.")

# OTHER METHOD
with open("file_1.txt") as f:
    text = f.read()
    if ("twinkle" in text):
        print(f"Yes, the file contains the word Twinkle.")
    else:
        print("The file does not contain the word Twinkle.")