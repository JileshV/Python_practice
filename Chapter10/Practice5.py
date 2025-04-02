from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book_ticket(self, fro, to):
        print(f"The ticket for train no.{self.trainNo}, is booked from {fro} to {to}.")

    def get_status(self):
        print(f"The train no.{self.trainNo}, is running on time.")

    def get_fare(self, fro, to):
        print(f"The ticket fare for train no.{self.trainNo}, from {fro} to {to} is {randint(400, 1500)}.")

c = Train(22944)
c.book_ticket("Kalyan", "Chinchwad")
c.get_status()
c.get_fare("Kalyan", "Chinchwad")