from django.db import models


class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    subject1=models.IntegerField()
    subject2=models.IntegerField()