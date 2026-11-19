from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    registration_date = models.DateField()
    age = models.IntegerField(default=0)
    phone_number = models.CharField()
    

    def __str__(self):
        return self.name

    