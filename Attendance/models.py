from django.db import models
from django.utils import timezone

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name

class TeacherCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.name} - {self.course.name}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now=True, null=True)
    check_out = models.DateTimeField(null=True, blank=True)  
    notes = models.TextField()

    def __str__(self):
        return f"Attendance for {self.student.first_name} on {self.check_in}"
 