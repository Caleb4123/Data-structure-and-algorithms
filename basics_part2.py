class car():
    def __init__(self,colour,number_seats,number_wheels):
        self.colour = colour
        self.number_seats = number_seats
        self.number_wheels = number_wheels
    def enter(self):
        self.colour = input("Enter the colour: ")
        self.number_seats = int(input("Enter the number of seats: "))
        self.number_wheels = int(input("Enter the number of wheels: "))
    def output(self):
        print(self.colour)
        print(self.number_seats)
        print(self.number_wheels)

object1 = car("red",6,4)
object1.output()
object1.enter()
object1.output()

