from django.db import models

import datetime
from django.utils import timezone
from tinymce.models import HTMLField
from photologue.models import (ImageModel,
                              Gallery,
                              Photo)

PIANO = 'Piano'
SAXOPHONE = 'Saxophone'
GUITAR = 'Guitare'
BATTERY = 'Batterie'
FLUTE = 'Flute'
INSTRUMENTS = (
    (PIANO, 'Piano'),
    (SAXOPHONE, 'Saxophone'),
    (GUITAR, 'Guitare'),
    (BATTERY, 'Batterie'),
    (FLUTE, 'Flute'),
)

################################################################################
# CONSTANTES (CONSTANTS)
################################################################################
HELP_TEXT_FORMAT_DATE = "Le format de la date est JJ-MM-AAAA"


# =======================================================
# CLASSE ABSTRAITES
# =======================================================
class Metadata(models.Model):
    actif = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True,
                                    help_text='HELP_TEXT_FORMAT_DATE', )
    date_modification = models.DateTimeField(auto_now=True,
                                    help_text=HELP_TEXT_FORMAT_DATE, )

    class Meta:
        abstract = True



class image_model(ImageModel):
    pass
# =======================================================
# Generic Model
# =======================================================

class Generique(Metadata):
    titreAcceuil = models.CharField(max_length=255)

    texteAcceuil = models.TextField()
    texteContact = models.TextField()


# =======================================================
# Teacher Model
# =======================================================
class Professeurs(Metadata):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    biographie = models.TextField()
    #photo = models.ForeignKey(image_model,blank=True)
    photo = models.OneToOneField(Photo,primary_key=True,blank=True)


    def __unicode__(self):
        return "%s  %s" % (self.nom, self.prenom)


# =======================================================
# Cours Model
# =======================================================

class Cours(Metadata):
    professeurs = models.ManyToManyField(Professeurs)
    instrument = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.FloatField()




# =======================================================
# Gallerie Model
# =======================================================
class Gallerie(Metadata):
    photos = models.ImageField(upload_to =
                               'media/photos/',
                               default =
                               'media/photos/none/no-img.jpg')




# =======================================================
# Blog Model
# =======================================================


class Blog(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.creation_date < now
    was_published_recently.admin_order_field = 'creation_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    author = models.CharField(max_length=60)
    creation_date = models.DateTimeField('date published')
    comment = models.TextField()

    def __unicode__(self):
        return self.author + self.comment[:10]



# class Instrument(Metadata):
#     instr_name = models.CharField(max_length=40)

#     def __unicode__(self):
#         return self.instr_name








# class Teacher(Metadata):
#     name = models.CharField(max_length=40)
#     surname = models.CharField(max_length=40)
#     instruments = models.ManyToManyField(Instrument)
#     biography = models.TextField()

#     def __unicode__(self):
#         return self.name + ' ' + self.surname

#     def instruments_taught(obj):
#         instrument_list = ', '.join([x.__unicode__() for x in obj.instruments.all()])
#         return instrument_list

#     instruments_taught.admin_order_field = 'name'
#     instruments_taught.boolean = False
#     instruments_taught.short_description = 'Instruments taught'


# =======================================================
# Media Model
# =======================================================


# class Media(Metadata):
#     title  = models.CharField(max_length=100)
#     description = models.TextField()
#     date_pub = models.DateTimeField('Date Publication')
#     categori = models.CharField(max_length = 60,
#         choices=,
#         default = )


#     class Meta:
#         abstract = True
