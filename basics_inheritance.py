class car():
    def __init__(self,tires,colour,fuel,size):
        self.tires = tires
        self.colour = colour
        self.fuel = fuel
        self.size = size
    def getter(self):
        return self.colour
    def setter(self,new_colour):
        self.colour = new_colour
    def show(self):
        print("tires - {},colour - {},fuel - {}, size - {}".format(self.tires,self.colour,self.fuel,self.size))
#child class
class BMW(car):
    def __init__(self,tires,colour,fuel,size,turbo,model):
        #super keyword
        super().__init__(tires,colour,fuel,size)
        self.turbo = turbo
        self.model = model
    def show(self):
        print("tires - {},colour - {},fuel - {}, size - {},turbo - {},model - {}".format(self.tires,self.colour,self.fuel,self.size,self.turbo,self.model))
#testing inheritance
object1=BMW(4,"blue","electric","large","yes","X5")
object1.show()
object1.setter("silver")
object1.show()
c = object1.getter()
print(c)