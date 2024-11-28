from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student/add/', StudentCreateView.as_view(), name='student_add'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/add/', CourseCreateView.as_view(), name='course_add'),
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/add/', TeacherCreateView.as_view(), name='teacher_add'),
    path('teacher/<int:pk>/edit/', TeacherUpdateView.as_view(), name='teacher_edit'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),
    path('attendances/', AttendanceListView.as_view(), name='attendance_list'),
    path('attendance/<int:pk>/', AttendanceDetailView.as_view(), name='attendance_detail'),
    path('attendance/add/', AttendanceCreateView.as_view(), name='attendance_add'),
    path('attendance/<int:pk>/edit/', AttendanceUpdateView.as_view(), name='attendance_edit'),
    path('attendance/<int:pk>/delete/', AttendanceDeleteView.as_view(), name='attendance_delete'),
]
