#create a menu for student

from database import create_table_teacher, add_teacher, get_teachers, close_database, delete_entry
from subject import view_subjects
create_table_teacher

teacher_menu = """
1. Add a teacher
2. List of all teacher
3. Delete a teacher
4. Go back to the main menu

Select your choice: """

def prompt_add_teacher():
    given_name = input("Enter first name: ")
    name_last = input("Enter last name: ")
    add_teacher(given_name, name_last)

def view_teachers(teachers):
    print("All teachers")
    for teacher in teachers:
        print(f"--------------------")
        print(f"Name of teachers: {teacher[0]} {teacher[1]}")

def remove_teacher():
    teacher = input("Last name of teacher you want to delete: ")
    delete_entry(teacher)

welcome_teacher = "Teacher Menu"
print(welcome_teacher)

user_input = input(teacher_menu)

while (user_input != 4):
    if user_input == "1":
        prompt_add_teacher()
    elif user_input == "2":
        view_teachers(get_teachers())
    elif user_input == "3":
        remove_teacher()
    elif user_input == "4":
        print("4")
    else:
        print ("Invalid options, try again!")

    user_input = input(teacher_menu)
