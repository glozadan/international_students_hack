from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, unique = True)
    username = models.CharField(max_length = 50, unique = True)
    password = models.CharField(max_length = 50)
    student_phone = models.CharField(max_length = 20)
    birthdate = models.DateField()
    country = models.CharField(max_length = 50)
    last_grade = models.CharField(max_length = 30)
    last_gpa = models.CharField(max_length = 5)
    social_network = models.CharField(max_length = 50)
    tutor_phone = models.CharField(max_length = 20, blank = True)

    def __str__(self):
        return self.email