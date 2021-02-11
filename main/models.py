from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
