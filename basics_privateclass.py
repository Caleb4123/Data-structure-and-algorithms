class user():
    #hidden variable
    __password = "password123"
    def __init__(self,name,email,username):
        self.name = name
        self.email = email
        self.username = username
    #function to get password
    def getter(self):
        return self.__password
    #set password
    def setter(self):
        current_password = input("Enter your current password: ")
        if current_password == self.__password:
            new_password = input("Enter the new password: ")
            self.__password = new_password
        else:
            print("Incorrect password")
    def output(self):
        print("Your username is",self.username)
        print("Your name is",self.name)
        print("Your password is",self.__password)
        print("Your email is", self.email)

#object creation
object1 = user("caleb","caleb@gmail.com","caleb123")
print(object1.getter())
object1.setter()
object1.output()