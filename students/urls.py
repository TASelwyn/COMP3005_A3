# COMP 3005 Assignment 3
#
# Author: Thomas Selwyn
# Date: November 2025
#
from django.urls import path
from . import views

urlpatterns = [
    path("", views.showStudentUI, name="ui"),
    path("list", views.getStudents, name="list"),
    path("add", views.addStudent, name="add"),
    path("update/<int:student_id>", views.updateStudent, name="update"),
    path("delete/<int:student_id>", views.deleteStudent, name="delete")
]