from django.db import models
from accounts.models import Student, Teacher

# Create your models here.
class Course (models.Model):
    title = models.CharField (max_length=150)
    description = models.CharField(max_length=250, default="No Description")
    student = models.ManyToManyField(Student, related_name='courses', blank=True)
    teacher = models.ManyToManyField(Teacher, related_name='teacher', blank=True)

    def __str__(self):
        return self.title

class Lesson (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="No Description")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title