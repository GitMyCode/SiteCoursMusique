from django.db import models

class Teacher(models.Model):
    PIANO = 'PIANO'
    SAXOPHONE = 'SAXOPHONE'
    GUITAR = 'GUITAR'
    BATTERY = 'BATTERY'
    INSTRUMENTS = (
        (PIANO, 'Piano'),
        (SAXOPHONE, 'Saxophone'),
        (GUITAR, 'Guitare'),
        (BATTERY, 'Batterie'),
    )
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    instrument = models.CharField(max_length=20,
                                    choices=INSTRUMENTS,
                                    default=PIANO)
    def __unicode__(self):
       return self.name +' ' + self.surname + ' ' + self.instrument

class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)

    def __unicode__(self):
       return self.name +' ' + self.surname
