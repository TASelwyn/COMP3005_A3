# COMP 3005 Assignment 3
#
# Author: Thomas Selwyn
# Date: November 2025
#
from django.db import models

class Student(models.Model):
    # Django specific schema (Autofield is auto-increm integer)
    student_id = models.AutoField(primary_key=True)
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    email = models.TextField(unique=True, null=False)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'students'