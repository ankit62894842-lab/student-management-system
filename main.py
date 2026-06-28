from funtions.add_student import add_student
from funtions.load_student import load_students
from funtions.save_student import save_students
from funtions.search_student import search_student
from funtions.show_menu import show_menu
from funtions.view_student import view_students
from funtions.update_student import update_student
from funtions.delete_student import delete_student



if __name__ == "__main__" :

    students = []

    load_students()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
           delete_student()

        elif choice == "6":
            save_students()

        elif choice == "7":
            print("Thank You!")
            break
                
        else:
            print("Invalid Choice! Please try again.")