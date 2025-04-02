class Programmers:
    def __init__(self, name, language, dept):   #Using dunder method
        self.name = name
        self.language = language
        self.dept = dept

    def get_details(self):
        print(f"Name: {self.name}, Language: {self.language}, Department: {self.dept}")

jilesh = Programmers("Jilesh", "C++", "Desktop apps")
ronak = Programmers("Ronak", "React", "Web apps")
vikas = Programmers("Vikas", "C#", "Desktop automation")

jilesh.get_details()
ronak.get_details()
vikas.get_details()