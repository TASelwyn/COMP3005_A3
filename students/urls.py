from django.urls import path
from . import views

urlpatterns = [
    path("", views.showStudentUI, name="ui"),
    path("read", views.getStudents, name="read"),
    path("add", views.addStudent, name="add"),
    path("update/<int:student_id>", views.updateStudent, name="update"),
    path("delete/<int:student_id>", views.deleteStudent, name="delete")
]