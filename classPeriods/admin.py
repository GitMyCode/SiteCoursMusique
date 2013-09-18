from django.contrib import admin
from classPeriods.models import ClassPeriod

class ClassPeriodAdmin(admin.ModelAdmin):
    fields = ['teacher','instrument','start_time','end_time']
    
admin.site.register(ClassPeriod, ClassPeriodAdmin)