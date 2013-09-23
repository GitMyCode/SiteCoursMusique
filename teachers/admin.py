from django.contrib import admin
from teachers.models import Teacher, Student, ClassPeriod

class ClassPeriodInline(admin.TabularInline):
    model = ClassPeriod
    extra = 5

class TeacherAdmin(admin.ModelAdmin):
    fields = ['name', 'surname']
    inlines = [ClassPeriodInline]

admin.site.register(Teacher, TeacherAdmin)