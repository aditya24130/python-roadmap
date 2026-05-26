import json

class Student:
    def __init__(self, name, age, grade, ):
        self.name = name
        self.age = age
        self.grade = grade
        
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
        }

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Student(**student) for student in data]

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error reading JSON file.")
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)


def add_student(students):

    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")


        student = Student(name, age, grade,)

        students.append(student)

        save_students(students)

        print("Student added successfully!")

    except ValueError:
        print("Invalid age! Please enter a number.")


def list_students(students):

    if not students:
        print("No student records found.")
        return

    print("\nStudent Records:")

    for i, student in enumerate(students, start=1):

        print(
            f"{i}. Name: {student.name}, "
            f"Age: {student.age}, "
            f"Grade: {student.grade}, "
           
        )

def search_student(students):

    try:
        search_age = int(input("Enter age to search: "))

        found = False

        for student in students:

            if student.age == search_age:

                print(
                    f"Found -> Name: {student.name}, "
                    f"Age: {student.age}, "
                    f"Grade: {student.grade}, "
                )

                found = True

        if not found:
            print("No students found with this age.")

    except ValueError:
        print("Please enter valid age!")


def main():

    students = load_students()

    while True:

        print("\n--- Student Record System ---")
        print("1. Add Student")
        print("2. List Students")
        print("3. Search Student By Age")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            list_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


main()