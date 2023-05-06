from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_id = models.IntegerField(verbose_name='Student ID')
    firstname = models.CharField(max_length=255, verbose_name='First Name')
    lastname = models.CharField(max_length=255, verbose_name='Last Name')
    faculty = models.CharField(max_length=255, verbose_name='Faculty')
    student_gpa = models.FloatField(verbose_name='GPA')


class Grades(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment_1 = models.IntegerField()
    assignment_2 = models.IntegerField()
    assignment_3 = models.IntegerField()


class Instructor(models.Model):
    instructor_id = models.IntegerField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    dateofjoin = models.DateField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


