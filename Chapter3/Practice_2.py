letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

name = input("Please Enter your name: ")
date = input("Enter today's date: ")
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))