from modeltranslation.translator import translator, TranslationOptions
from sitemusique.core.models import Generique,Professeurs,Cours

class GeneriqueTranslationOptions(TranslationOptions):
    fields = ('texteAcceuil','texteContact',)

translator.register(Generique, GeneriqueTranslationOptions)




class CoursTranslationOptions(TranslationOptions):
    fields = ('instrument',)

translator.register(Cours, CoursTranslationOptions)


