#create a menu for student


from database import create_table_subject, add_subject, get_subjects, delete_entry, close_database

create_table_subject()

subject_menu = """
1. Add a subject
2. List of all subjects
3. Delete a subject
4. Go back to the main menu

Select your choice: """

def prompt_add_subject():
    subject_code = input("Enter subject code: ")
    subject_name = input("Enter subject name: ")
    add_subject(subject_code, subject_name)

def view_subjects(subjects):
    print("All subjects")
    for subject in subjects:
        print(f"--------------------")
        print(f"Subject code: {subject[0]}\nSubject Name: {subject[1]}")

def remove_subject():
    subject = input("Name of subject you want to delete: ")
    delete_entry(subject)


welcome_subject = "Subject Menu"
print(welcome_subject)
user_input = input(subject_menu)

while (user_input != 4):
    if user_input == "1":
        prompt_add_subject()
        print("f{subject_code}{subject_name}")
    elif user_input == "2":
        view_subjects(get_subjects())
    elif user_input == "3":
        remove_subject()
    elif user_input == "4":
        import main
        main()
    else:
        print ("Invalid options, try again!")

    user_input = input(subject_menu)
