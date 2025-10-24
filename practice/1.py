def main():
    students = {
        "Alice": {"Math": 90, "English": 85},
        "Bob": {"Math": 78, "Science": 88}
    }

    x = students.keys()
    print(x)
    print(students["Alice"]["Math"])
    print(students["Bob"]["Science"])
    students["Alice"]["Science"] = 70
    print(students["Alice"])
    students["Bob"]["Math"] = 82
    print(students["Bob"])

    students.update({"Charlie": {"Sience": 90, "Math":60 }})
    print(students)

    del students["Alice"]["Math"]
    print(f"Final dictionary: {students}")

    students = del_student(students, "Bob", "Math")
    print(f"Delete: {students} ")

    add_student(students, "Ann", {"Science": 90, "English": 77})
    print(f"Add s func: {students}")

    upgrade_grade(students, "Ann", "Science", 99)
    print(students)

    add_subject(students, "Ann", "Biology", 77)
    print(students)


def del_student(students, name, subject):
    del students[name][subject]
    return students

def add_student(students, name, subject):
    students[name] = subject
    return

def upgrade_grade(students, name, subject, new_score):
    students[name][subject] = new_score

def add_subject(students, name, subject, score):


def print_students(students, name):

def get_average(students, name):
main()