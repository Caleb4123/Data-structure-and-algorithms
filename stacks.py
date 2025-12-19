class stack:
    def __init__(self,total):
        self.var = []
        self.total = total
    def push(self,element):
        if len(self.var) < self.total:
            self.var.append(element)
            print(element,"has been pushed in the stack")
        else:
            print("The stack is full")
    def pop(self):
        if len(self.var) == 0:
            print("The stack is empty")
        else:
            print(self.var[-1],"has been removed from the stack")
            self.var.pop(-1)
    def peek(self):
        if len(self.var) == 0:
            print("The stack is empty")
        else:
            print(self.var[-1])
    def size(self):
        if len(self.var) == 0:
            print("The stack is empty")
        else:
            print(len(self.var))               
    def display(self):
        if len(self.var) == 0:
            print("The stack is empty")
        else:
            for i in self.var:
                print(i)
    def empty(self):
        if len(self.var) == 0:
            print("The stack is empty")        
        else:
            print("The stack is not empty")
    def full(self):
        if len(self.var) == self.total:
            print("The stack is full") 
        else:
            print("stack is not full")
#creating a stack object
stack_object = stack(5)
stack_object.empty()
stack_object.push(12)
stack_object.push(21)
stack_object.push(8)
stack_object.push(3)
stack_object.push(17)
stack_object.full()
stack_object.display()
stack_object.empty()
stack_object.peek()
stack_object.size()
stack_object.pop()
stack_object.display()
stack_object.full()