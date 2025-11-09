from django.urls import path
from . import views

urlpatterns = [
    path("", views.showStudentUI, name="ui"),
    path("read", views.getAllStudents, name="read"),
    path("add", views.addStudent, name="add")

]