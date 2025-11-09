from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from students.DatabaseFunctions import *

# Show student UI
def showStudentUI(request):
    return render(request, "students/user_interface.html", {"students": getAllStudents()})

# GET Students
def getStudents(request):
    return JsonResponse(getAllStudents(), safe=False, json_dumps_params={'indent': 4})

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
        student = addStudent(first_name, last_name, email, enrollment_date)
        return JsonResponse({"student_id": student.student_id, "message": "Successfully added student"})

    except Exception as e:
        return HttpResponseBadRequest(str(e))

# Update Students
def updateStudentEmail(request):
    # Must be POST
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    try:
        # Decode body (x-www-form-urlencoded)
        student_id = request.POST.get("student_id")
        new_email = request.POST.get("new_email")

        # Update email and return
        student = updateStudentEmail(student_id, new_email)
        return JsonResponse({"student_id": student.student_id, "message": "Successfully updated " + student.first_name + "'s email with " + student.email})

    except Exception as e:
        return HttpResponseBadRequest(str(e))