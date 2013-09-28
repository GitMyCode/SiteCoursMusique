from django.db import models

import datetime
from django.utils import timezone


# =======================================================
# Blog Model
# =======================================================

class New(models.Model):

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
   new = models.ForeignKey(New)
   author = models.CharField(max_length=60)
   creation_date = models.DateTimeField('date published')
   comment = models.TextField()

   def __unicode__(self):
      return self.author + self.comment[:10]


# =======================================================
# Teacher Model
# =======================================================
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
    (FLUTE,'Flute'),
)

class Teacher(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    def __unicode__(self):
       return self.name +' ' + self.surname

class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)

    def __unicode__(self):
       return self.name +' ' + self.surname

class ClassPeriod(models.Model):
    teacher = models.ForeignKey(Teacher)
    start_time = models.DateTimeField('Start time')
    end_time = models.DateTimeField('End time')
    instrument = models.CharField(
        max_length=20,
        choices=INSTRUMENTS,
        default=PIANO
    )

    def __unicode__(self):
        if all(getattr(self.start_time,x)==getattr(self.end_time,x) for x in ['year','month','day']):
            return '%s: %s, %s : %s' % (self.instrument,self.start_time.strftime('%a %b %d %Y'),self.start_time.strftime('%H:%m'),self.end_time.strftime('%H:%m'))
        else:
            return '%s: %s to %s' % (self.instrument, self.start_time.strftime('%a %b %d %Y:%H:%m'),self.end_time.strftime('%a %b %d %Y:%H:%m'))
