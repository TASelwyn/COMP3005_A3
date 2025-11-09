from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from students import DatabaseFunctions as postgres

# Show student UI
def showStudentUI(request):
    return render(request, "students/user_interface.html", {"students": postgres.getAllStudents()})

# GET Students
def getStudents(request):
    return JsonResponse(postgres.getAllStudents(), safe=False, json_dumps_params={'indent': 4})

# ADD Students
def addStudent(request):
    # Must be POST
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        # Decode body (x-www-form-urlencoded)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        enrollment_date = request.POST.get("enrollment_date")

        # Add student and return
        student = postgres.addStudent(first_name, last_name, email, enrollment_date)
        return JsonResponse({"student_id": student.student_id, "message": "Successfully created " + first_name + " " + last_name + "."})

    except Exception as e:
        return HttpResponseBadRequest(str(e))

# Update Students
def updateStudent(request, student_id):
    # Must be POST/GET
    if not request.method in ["GET", "POST"]:
        return HttpResponseNotAllowed(["POST", "GET"])

    if request.method == "POST":
        try:
            # Decode body (x-www-form-urlencoded)
            new_email = request.POST.get("email")

            # Update email and return
            student = postgres.updateStudentEmail(student_id, new_email)
            return JsonResponse({"student_id": student.student_id, "message": "Successfully updated " + student.first_name + "'s email with " + student.email})

        except Exception as e:
            return HttpResponseBadRequest(str(e))

    if request.method == "GET":
        return render(request, "students/update_email.html", {"student": postgres.getStudent(student_id)})

def deleteStudent(request, student_id):
    # Must be POST/GET
    if not request.method in ["GET", "POST"]:
        return HttpResponseNotAllowed(["POST", "GET"])

    try:
        # Delete Student and return
        student = postgres.deleteStudent(student_id)
        return JsonResponse({"email": student.email, "message": "Successfully deleted " + student.first_name + " " + student.last_name + " from the database"})

    except Exception as e:
        return HttpResponseBadRequest(str(e))