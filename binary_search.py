number_items = int(input(("How many items are in the list? ")))
var = []
for i in range(number_items):
   item = int(input("Enter the item to add to the list: "))
   var.append(item)

search = int(input("Enter the item to search for in the list: "))
high = number_items - 1
low = 0
check = 0
found = False
while high >= low and search != var[check]:
   check = (high + low)// 2
   if search == var[check]:
      found = True
      print("Item found in position", check + 1)
   elif search > var[check]:
      low = check + 1 
   elif search < var[check]:
      high = check - 1


if found == False:
   print("The item is not located in the list")

