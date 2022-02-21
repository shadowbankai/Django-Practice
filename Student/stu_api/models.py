from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    roll_number = models.IntegerField(max_length=4)
    marks = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name



