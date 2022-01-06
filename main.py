# Create a Learning Management System
# Create, list, and delete Student
# Create, list, and delete Teacher
# Create, list, and delete Subject
# Create class of subject with an assigned teacher
#----subject - multiple class
#----teacher multiple class
# Add student to a class
#----assign student to multiple classes
# View list of students in a class
# View list of class in a given student
# View list of class of a given teacher   

def main_main(): 
    main_menu = """
    1. Student
    2. Teacher
    3. Subjects
    4. Display a class
    5. Exit

    Select your choice: """
    
    print("""
     ---------------------------------------------
    | WELCOME TO YOUR LEARNING MANAGEMENT SYSTEM! |
     ---------------------------------------------
    """)


    user_input = input(main_menu)
    while (user_input != 4):
        if user_input == "1":
            import student 
            student.student_menu
        elif user_input == "2":
            import teacher 
            teacher.teacher_menu
        elif user_input == "3":
            import subject
            subject.subject_menu
        elif user_input == "4":
            import classroom
            classroom.class_menu
        elif user_input == "5":
            exit()
        else:
            print ("Invalid options, try again!")
        user_input = input(main_menu)
main_main()