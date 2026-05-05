# application logic
import app.db as db

class ServiceError(Exception):pass

def add_student(student):
  if not 18 <= student["age"] <= 120:
      raise ServiceError(f'Student age is illegal: {student["age"]}')

  return db.add_student(student)


def get_students():
    return db.get_students()


def get_student(student_id):
    return db.get_student(student_id)


def update_student(student_update):
    return db.update_student(student_update)


def delete_student(student_id):
    return db.delete_student(student_id)