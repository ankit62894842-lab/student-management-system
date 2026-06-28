from funtions.save_student import save_students
from funtions.data import students

def update_student() :
    name = str(input("search name : "))
    id = int(input("enter the id : "))
    new_name = str(input("give the new name : "))
    new_id = int(input("enter new id :"))
    update = False
    for student in students :
        if student["id"] == id and student["name"].lower() == name.lower() :
            student["name"] = new_name
            student["id"] = new_id
            save_students()
            
            update = True
            break
    if not update :
        print("something is wrong. not updated")