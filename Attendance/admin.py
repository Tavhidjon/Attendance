from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(TeacherCourse)
admin.site.register(Attendance)
