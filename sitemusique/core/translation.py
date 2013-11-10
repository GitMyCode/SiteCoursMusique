from modeltranslation.translator import translator, TranslationOptions
from models import Generique,Professeurs,Cours

class GeneriqueTranslationOptions(TranslationOptions):
    fields = ('texteAcceuil','texteContact',)

translator.register(Generique, GeneriqueTranslationOptions)




class CoursTranslationOptions(TranslationOptions):
    fields = ('instrument',)

translator.register(Cours, CoursTranslationOptions)

