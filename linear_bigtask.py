while True:
    print("====== MAIN MENU ======")
    print("1. List operations")
    print("2. Tuple operations")
    print("3. Dictionary operations")
    print("4. Set operations")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        list1 = []
        while True:
            print("--- List menu ---")
            print("1. Add element")
            print("2. Remove element")
            print("3. Display list")
            print("4. Back to main menu")
            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                element = input("Enter the element: ")
                list1.append(element)
            elif choice2 == 2:
                element = input("Enter the element: ")
                list1.remove(element)
            elif choice2 == 3:
                print(list1)
            else:
                break

    elif choice == 2:
        tuple1 = ()
        while True:
            print("--- Tuple menu ---")
            print("1. Create tuple")
            print("2. Display tuple")
            print("3. Count element")
            print("4. Back to main menu")
            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                element = input("Enter the values, seperated by a space")
                var = tuple1(element.split())
            elif choice2 == 2:
                print(var)
            elif choice2 == 3:
                print(len(tuple1))
            else:
                break 
    
    elif choice == 3:
        dictionary1 = {}
        while True:
            print("--- Dictionary menu ---")
            print("1. Add key-value pair")
            print("2. Delete key")
            print("3. Display dictionary")
            print("4. Back to main menu")
            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                key = input("Enter the value, of the key")
                definition = input("Enter the definition, of the key")
                dictionary1[key] = definition
            elif choice == 2:
                element = input("What value should be removed: 2")
                del dictionary1[key]
            elif choice == 3:
                print(dictionary1)
            else:
                break

    elif choice == 4:
        set1 = set()
        while True:
            print("--- Set menu ---")
            print("1. Add element")
            print("2. Remove element")
            print("3. Display set")
            print("4. Back to main menu")
            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                element = input("What value should be added: ")
                set1.add(element)
            elif choice2 == 2:
                element = input("What value should be removed: ")
                set1.remove(element)
            elif choice2 == 3:
                print(set1)
            else:
                break

