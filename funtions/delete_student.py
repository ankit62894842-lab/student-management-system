from funtions.data import students
from funtions.save_student import save_students

def delete_student() :

    name = str(input("search name : "))
    id = int(input("enter the id : "))
    delete = False

    for student in students :

        if student["id"] == id and student["name"].lower() == name.lower() :
            students.remove(student)
            save_students()
            
            delete = True
            break

        if not delete :
            print("not deleted")