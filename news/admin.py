from django.contrib import admin
from news.models import New, Comment

class CommentInline(admin.TabularInline):
   model = Comment
   extra = 1

class NewAdmin(admin.ModelAdmin):
   fieldsets = [(None,{'fields':['title', 'content']}),('Date de creation', {'fields': ['creation_date'], 'classes': ['collapse']}),]
   list_filter = ['creation_date']
   date_hierarchy = 'creation_date'
   inlines = [CommentInline]
admin.site.register(New, NewAdmin)