from django.db import models


class ClassPeriod(models.Model):
    start_time = models.DateTimeField('Start time')
    end_time = models.DateTimeField('End time')
    teacher = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)

    def __unicode__(self):
        if all(getattr(self.start_time,x)==getattr(self.end_time,x) for x in ['year','month','day']):
            return '%s (%s): %s, %s : %s' % (self.teacher, self.instrument,self.start_time.strftime('%a %b %d %Y'),self.start_time.strftime('%H:%m'),self.end_time.strftime('%H:%m'))
        else:
            return '%s (%s): %s to %s' % (self.teacher, self.instrument, self.start_time.strftime('%a %b %d %Y:%H:%m'),self.end_time.strftime('%a %b %d %Y:%H:%m'))
