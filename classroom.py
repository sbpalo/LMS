

class_menu = """
1. List of classes
2. 
3. 
4. 

Select your choice: """

welcome_class = "Class Menu"
print(welcome_class)

user_input = input(class_menu)

while (user_input != 4):
    if user_input == "1":
        print("1")
    elif user_input == "2":
        print("1")
    elif user_input == "3":
        print("1")
    elif user_input == "4":
        import main
        main()
    else:
        print ("Invalid options, try again!")

    user_input = input(class_menu)