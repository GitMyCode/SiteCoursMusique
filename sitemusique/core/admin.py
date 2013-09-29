from django.contrib import admin
from models import Blog, Comment, Teacher, Instrument


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields': ['title', 'content']}
         ),
        ('Date de creation',
            {'fields': ['creation_date'], 'classes': ['collapse']}
         ),
    ]
    list_display = ('title', 'was_published_recently')
    list_filter = ['creation_date']
    date_hierarchy = 'creation_date'
    inlines = [CommentInline]
admin.site.register(Blog, BlogAdmin)


class InstrumentInline(admin.TabularInline):
    model = Teacher.instruments.through


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'instruments_taught')
    fields = ['name', 'surname']
    inlines = [InstrumentInline]


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Instrument)
