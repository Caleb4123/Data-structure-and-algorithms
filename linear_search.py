number_of_items = int(input("How many items should be in the list? "))
var = []
for i in range(number_of_items):
    choice = input("Is the item to add a string or integer? ")
    if choice == "string":
        item = input("Enter the item to add: ")
    elif choice == "integer":
        item = int(input("Enter the item to add: "))
    var.append(item)
print(var)
search_choice = input("Is the item to search for a string or integer? ")
if search_choice == "string":
    search = input("What item should be searched for? ")
elif search_choice == "integer":
    search = int(input("What item should be searched for? "))
count = 0
search_valid = False
while search_valid != True and count > number_of_items:
    for i in range(number_of_items):
        if var[count] == search:
            search_valid = True
            print(search_valid)
        else:
            search_valid = False
            count = count+1
if search_valid == True:
    print("The item is in the list")
else:
    print("The item is not in the list")