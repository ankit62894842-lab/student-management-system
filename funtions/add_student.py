from funtions.save_student import save_students
from funtions.data import students

students = []
def add_student() :
        student_id = int(input("id : "))
        name = str(input("name : "))
        age =int(input("age : "))
        student = {
        "id": student_id,
        "name": name,
        "age": age }

        students.append(student)
        save_students()
        print("Student Added Successfully!")