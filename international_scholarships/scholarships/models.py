from django.db import models
from organizations.models import Organization

# Create your models here.

class Scholarship(models.Model):
    types = [
        ('Full scholarship', 'Full scholarship'),
        ('Partial scholarship', 'Partial scholarship'),
        ('Merit-Based scholarship', 'Merit-Based scholarship'),
        ('Financial scholarship', 'Financial scholarship')
    ]

    grades = [
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('PhD', 'PhD'),
        ('Research', 'Research')
    ]

    organization = models.ForeignKey(Organization, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    university = models.CharField(max_length = 40)
    grade_level = models.CharField(max_length = 15, choices = grades)
    field = models.CharField(max_length = 30)
    program = models.CharField(max_length = 30)
    scholarship_duration = models.CharField(max_length = 30)
    country = models.CharField(max_length = 25)
    scholarship_type = models.CharField(max_length = 25, choices = types)

    class Meta:
        db_table = 'scholarships'
    
    def __str__(self):
        return self.name