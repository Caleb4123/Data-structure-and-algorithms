var = []
def bubble(list1):
    length = len(list1)
    for i in range(length):
        for j in range(0,length-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]          

def linear(list1,item_search):
    length = len(list1)
    found = False
    for i in range(length):
        if list1[i] == item_search:
            print("The item has been found at index",i)
            found = True
            break
    if found == False:
        print("The item is not in the list")

def binary(list1,item_search):
    length = len(list1)
    found = False
    while not found:
        half = i[length/2]
        if half == item_search:
            print("The item has been found")
            found = True
            break
    else:
        print("The item is not in the list")


while True:
    print("===== MENU =====")
    print("1. Input the array (do first)")
    print("2. Bubble sort")
    print("3. Linear search")
    print("4. Binary search")
    print("5. Display array")
    print("6. Exit")
    option = int(input("Enter your choice: "))
    if option == 1:
        var = []
        number_of_items = int(input("Enter the number of items to add to the list: "))
        for i in range(number_of_items):
            item = int(input("Enter the item to add to the list: "))
            var.append(item)
        print("Array stored successfully")
    elif option == 2:
        if len(var) < 0:
            print("There is no array to sort")
        elif len(var) > 0:
            bubble(var)
            print(var)
    elif option == 3:
        if len(var) < 0:
            print("There is no array to search")
        elif len(var) > 0:
            search = int(input("Enter the item to be searched for: "))
            linear(var,search)
    elif option == 4:
        if len(var) < 0:
            print("There is no array to search")
        elif len(var) > 0:
            search = int(input("Enter the item to be searched for: "))
            binary(var,search)