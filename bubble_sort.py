var = []
number_of_items = int(input("How many items are in the list? "))
for i in range(number_of_items):
    item = int(input("Enter the item for the list: "))
    var.append(item)

for i in range(number_of_items):
    for j in range(0,number_of_items-1):
        if var[j] > var[j+1]:
            var[j],var[j+1] = var[j+1],var[j]

print(var)