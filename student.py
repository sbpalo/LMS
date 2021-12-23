#create a menu for student

from database import create_table_student, add_student, get_students, delete_entry, close_database

create_table_student()
student_menu = """
1. Add a student
2. List of all students
3. Delete a student
4. Go back to the main menu

Select your choice: """

def prompt_add_student():
    first_name = input("Enter first name: ")
    middle_name = input("Enter middle name: ")
    last_name = input("Enter last name: ")
    add_student(first_name, middle_name, last_name)

def view_students(students):
    print("All students")
    for student in students:
        print(f"--------------------")
        print(f"Name of student: {student[0]} {student[2]}")

def remove_student():
    student = input("Last name of student you want to delete: ")
    delete_entry(student)

welcome_student = "Student Menu"
print(welcome_student)

user_input = input(student_menu)

while (user_input != 4):
    if user_input == "1":
        prompt_add_student()
    elif user_input == "2":
        view_students(get_students())
    elif user_input == "3":
        remove_student()
    elif user_input == "4":
        import main
        main.main_menu()
    else:
        print ("Invalid options, try again!")

    user_input = input(student_menu)
