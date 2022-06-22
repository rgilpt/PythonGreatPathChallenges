from django.db import models

# Create your models here.
class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    year = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='John')
    surname = models.CharField(max_length=100, blank=True, default='Doe')
    knows_python = models.BooleanField(default=False)
    likes_godot = models.BooleanField(default=False)
    rate_interest = models.IntegerField()

    class Meta:
        ordering = ['created']