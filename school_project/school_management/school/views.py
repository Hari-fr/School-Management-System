from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Teacher, Student

class HomeView(TemplateView):
    template_name = 'school/home.html'
    
class TeacherListView(ListView):
    model = Teacher
    template_name = 'school/teacher_list.html'
    context_object_name = 'teachers'
    
class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'school/teacher_detail.html'
    context_object_name = 'teacher'

class StudentListView(ListView):
    model = Student
    template_name = 'school/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student_detail.html'
    context_object_name = 'student'

