import json
from funtions.data import students

def load_students() :
        global students 
        try:
            with open("students.json", "r") as file:
                students.clear()
                students.extend(json.load(file))
        except FileNotFoundError:
            students = []

        except json.JSONDecodeError:
            students = []