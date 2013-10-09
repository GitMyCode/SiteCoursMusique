from django.contrib import admin
from models import (
                    Blog,
                    Comment,
                    Generique,
                    Professeurs,
                    Cours,
                    )
class general(admin.ModelAdmin):
    class Media:
        js = ('media/js/tiny_mce/tiny_mce.js', 'media/js/tiny_mce/textareas.js',)


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



class GeneriqueAdmin(general):
    list_display = ('texteAcceuil' , 'texteContact' )
    fields = ['texteAcceuil' , 'texteContact']

admin.site.register(Generique, GeneriqueAdmin)

class CoursAdmin(general):
    list_display = ('instruments' , 'prix', 'description' )
    fields = ['instruments' , 'prix', 'description','professeurs']
admin.site.register(Cours, CoursAdmin)




class ProfesseursAdmin(general):
    list_display = ('prenom' , 'nom', 'biographie' )
    fields = ['nom', 'prenom', 'biographie']

admin.site.register(Professeurs, ProfesseursAdmin)
