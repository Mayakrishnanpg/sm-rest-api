from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    born=models.CharField(max_length=255)
