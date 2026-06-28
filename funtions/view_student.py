from funtions.data import students

def view_students() :
        if len(students) == 0 :
            print("no student found")
            return

        for student in students :
            print(f"ID : {student['id']}")
            print(f"NAME  : {student['name']}")
            print(f"AGE : {student['age']} ")