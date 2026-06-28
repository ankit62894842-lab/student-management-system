from funtions.data import students

def search_student() :
        typeing_name = str(input(" name search "))
        found = False
        for student in students :
            if student["name"].lower() == typeing_name.lower() :

                print(f"id :  : {student['id']}")
                print(f"name :  : {student['name']}" )
                print(f"age :  : {student['age']}")

                found = True
                break
            if not found :
                print("name not found")