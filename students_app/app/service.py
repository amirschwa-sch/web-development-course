students = [
 {"id": 1, "name": "John Doe", "age": 20},
 {"id": 2, "name": "John Smith", "age": 22},
]

next_id = 3

def add_student(student):
    global next_id
    student["id"] = next_id
    next_id += 1
    students.append(student)
    return student


def get_students():
    return students


def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    raise KeyError(f"student not found: {student_id}")


def update_student(student_update):
    for student in students:
        if student["id"] == student_update["id"]:
            student.update(student_update)
            return student
    raise KeyError(f"student not found: {student_update['id']}")

def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return student
    raise KeyError(f"student not found: {student_id}")



