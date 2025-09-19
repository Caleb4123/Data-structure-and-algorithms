#class creation
class person():
    #constructor - initialising the variables
    def __init__(self,name,height,language,age):
        self.name = name
        self.height = height
        self.language = language
        self.age = age
    #function taking input
    def test(self):
        self.name = input("Enter the name: ")
        self.height = input("Enter the height: ")
        self.language = input("Enter the language: ")
        self.age = input("Enter the age: ")
    #function to display output
    def output(self):
        print(self.name)
        print(self.height)
        print(self.language)
        print(self.age)

#object creation
object1 = person("caleb",5.6,"english",15)
object2 = person("alan",4.2,"french",12)
#calling function with object
object1.output()
object2.output()