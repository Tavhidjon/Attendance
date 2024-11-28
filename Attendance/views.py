from django.views.generic import *
from django.urls import reverse_lazy
from .models import *

class HomeView(TemplateView):
    template_name = "home.html"

class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"

class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"
    context_object_name = "student"

class StudentCreateView(CreateView):
    model = Student
    template_name = "student_form.html"
    fields = '__all__'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    template_name = "student_form.html"
    fields = '__all__'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy('student_list')

class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"
    context_object_name = "courses"

class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"
    context_object_name = "course"

class CourseCreateView(CreateView):
    model = Course
    template_name = "course_form.html"
    fields = '__all__'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    template_name = "course_form.html"
    fields = '__all__'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = "course_confirm_delete.html"
    success_url = reverse_lazy('course_list')

class TeacherListView(ListView):
    model = Teacher
    template_name = "teacher_list.html"
    context_object_name = "teachers"

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "teacher_detail.html"
    context_object_name = "teacher"

class TeacherCreateView(CreateView):
    model = Teacher
    template_name = "teacher_form.html"
    fields = '__all__'
    success_url = reverse_lazy('teacher_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = "teacher_form.html"
    fields = '__all__'
    success_url = reverse_lazy('teacher_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = "teacher_confirm_delete.html"
    success_url = reverse_lazy('teacher_list')

class AttendanceListView(ListView):
    model = Attendance
    template_name = "attendance_list.html"
    context_object_name = "attendances"

class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = "attendance_detail.html"
    context_object_name = "attendance"

class AttendanceCreateView(CreateView):
    model = Attendance
    template_name = "attendance_form.html"
    fields = '__all__'
    success_url = reverse_lazy('attendance_list')

class AttendanceUpdateView(UpdateView):
    model = Attendance
    template_name = "attendance_form.html"
    fields = '__all__'
    success_url = reverse_lazy('attendance_list')

class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = "attendance_confirm_delete.html"
    success_url = reverse_lazy('attendance_list')
