from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=225)
    experience = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=225)
    date_birth = models.DateField()

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=225)
    duration = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


