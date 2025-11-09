from .models import Student


def getAllStudents() -> list[Student]:
    students = Student.objects.all().values()
    return list(students)

def addStudent(first_name: str, last_name: str, email: str, enrollment_date: str) -> Student:
    # Validate input
    if not all([first_name, last_name, email, enrollment_date]):
        raise Exception("Missing required fields")
    if Student.objects.filter(email=email).exists():
        raise Exception("Email already exists.")

    # Create
    student = Student.objects.create(first_name=first_name, last_name=last_name, email=email, enrollment_date=enrollment_date)
    return student

def updateStudentEmail(student_id: str, new_email: str) -> Student:
    # Validate input
    if not all([student_id, new_email]):
        raise Exception("Missing required fields")
    if not Student.objects.filter(student_id=student_id).exists():
        raise Exception("Student not found in database.")

    # Update
    student = Student.objects.update(student_id=student_id, email=new_email)
    return student

def deleteStudent(student_id: str) -> Student:
    # Validate input
    if not all([student_id]):
        raise Exception("Missing required fields")

    # Delete
    try:
        student = Student.objects.get(student_id=student_id)
        student.delete()
        return student
    except Student.DoesNotExist:
        raise Exception("Student not found in database.")
    except Exception:
        raise Exception("Failed to delete student.")