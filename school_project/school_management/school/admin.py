from django.contrib import admin
from .models import Teacher, Student

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('subject', 'hire_date')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'roll_number', 'teacher')
    search_fields = ('first_name', 'last_name', 'email', 'roll_number')
    list_filter = ('teacher',)

