from django.contrib import admin
from models import (
                    Blog,
                    Comment,
                    Professeurs
                    )


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




class ProfesseursAdmin(admin.ModelAdmin):
    # list_display = ('prenom' , 'nom', 'biographie' )
    # fields = ['nom', 'prenom', 'biographie']
    class Media:
        js = ('media/js/tiny_mce/tiny_mce.js', 'media/js/tiny_mce/textareas.js',)


admin.site.register(Professeurs, ProfesseursAdmin)
