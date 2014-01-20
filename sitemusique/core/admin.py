from django.contrib import admin
from photologue.models import ImageModel
from sitemusique.core.models import (
                    Blog,
                    Comment,
                    Generique,
                    Professeurs,
                    Cours,
                    Gallerie,
                    AutresServices,
                    )
class general(admin.ModelAdmin):
    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas.js',)


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
    list_display = ( 'titreAcceuil', 'texteAcceuil' , 'texteContact' )
    fields = ['titreAcceuil', 'texteAcceuil' , 'texteContact']

admin.site.register(Generique, GeneriqueAdmin)

class CoursAdmin(general):
    list_display = ('instrument_fr','instrument_en' , 'prix' )
    fields = ['instrument_fr','instrument' , 'prix', 'description','professeurs']
admin.site.register(Cours, CoursAdmin)


admin.site.register(Gallerie)

class ProfesseursAdmin(general):
    list_display = ('prenom' , 'nom' )
    fields = ['prenom','nom', 'biographie','photo']
admin.site.register(Professeurs, ProfesseursAdmin)


class AutresServicesAdmin(general):
    list_display = ('nom','prix')
    fields = ['nom','prix','description']

admin.site.register(AutresServices, AutresServicesAdmin)


