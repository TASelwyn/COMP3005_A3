from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from .models import Student
from django.shortcuts import redirect


# Show student UI
def showStudentUI(request):
    students = Student.objects.all().order_by("student_id")
    return render(request, "students/user_interface.html", {"students": students})

# GET Students
def getAllStudents(request):
    students = Student.objects.all().values()
    return JsonResponse(list(students), safe=False, json_dumps_params={'indent': 4})

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

        # Validate input
        if not all([first_name, last_name, email, enrollment_date]):
            return HttpResponseBadRequest("Missing required fields")
        if Student.objects.filter(email=email).exists():
            return HttpResponseBadRequest("Email already exists.")

        # Create
        student = Student.objects.create(first_name=first_name, last_name=last_name, email=email, enrollment_date=enrollment_date)
        return JsonResponse({"student_id": student.student_id, "message": "Successfully added student"})

    except Exception as e:
        return HttpResponseBadRequest(str(e))
