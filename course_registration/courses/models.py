from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    maximum_capacity = models.PositiveIntegerField()
    current_enrolled = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def is_full(self):
        return self.current_enrolled >= self.maximum_capacity


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrolled_courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self):
        return self.name
