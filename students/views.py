from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from .models import Student
import json


# Show student UI
def showStudentUI(request):
    students = Student.objects.all().order_by("student_id")
    return render(request, "students/user_interface.html", {"students": students})

# GET Students
def getAllStudents(request):
    students = Student.objects.all().values()
    return JsonResponse(list(students), safe=False, json_dumps_params={'indent': 4})
