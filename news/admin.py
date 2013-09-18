from django.contrib import admin
from news.models import New

class NewAdmin(admin.ModelAdmin):
    fields = ['title','content','creation_date']

admin.site.register(New, NewAdmin)