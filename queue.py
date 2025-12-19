class queue:
    def __init__(self,size):
        self.size = size
        self.var = []
    def enqueue(self,element):
        if len(self.var) < self.size:
            self.var.append(element)
        else:
            print("The queue is full")
    def dequeue(self):
        if len(self.var) != 0:
            self.var.pop(0)
        else:
            print("The queue is empty")
    def empty(self):
        if len(self.var) == 0:
            print("The queue is empty")
        else:
            print("The queue is not empty")
    def display(self):
        if len(self.var) != 0:
            for i in self.var:
                print(i)
        else:
            print("The queue is empty")
    def front(self):
        if len(self.var) != 0:
            print(self.var[0])
        else:
            print("The queue is empty")
    def rear(self):
        if len(self.var) != 0:
            print(self.var[-1])
        else:
            print("The queue is empty")
    def size_queue(self):
        print("The size of the queue is", len(self.var))

size1 = int(input("Enter the size for the queue: "))
object1 =  queue(size1)
while True:
    print("Menu: ")
    print("1: Enqueue")
    print("2. Dequeue")
    print("3. Empty")
    print("4. Display")
    print("5. Front")
    print("6. Rear")
    print("7. Size")
    print("8. Exit")
    user = int(input("Enter a choice: "))

    if user == 1:
        element = input("Enter the item to be placed into the queue: ")
        object1.enqueue(element)
    elif user == 2:
        object1.dequeue()
    elif user == 3:
        object1.empty()
    elif user == 4:
        object1.display()
    elif user == 5:
        object1.front()
    elif user == 6:
        object1.rear()
    elif user == 7:
        object1.size_queue()
    elif user == 8:
        break


        
