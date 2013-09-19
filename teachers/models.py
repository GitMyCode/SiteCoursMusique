from django.db import models

PIANO = 'PIANO'
SAXOPHONE = 'SAXOPHONE'
GUITAR = 'GUITAR'
BATTERY = 'BATTERY'
FLUTE = 'FLUTE'
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
