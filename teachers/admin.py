from django.contrib import admin
from teachers.models import Teacher, Student

class TeacherAdmin(admin.ModelAdmin):
    fields = ['name','surname','instrument']
    
admin.site.register(Teacher, TeacherAdmin)