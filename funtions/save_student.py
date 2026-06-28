import json

from funtions.data import students

def save_students():
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("Data Saved Successfully!")