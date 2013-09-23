from django.db import models
import datetime
from django.utils import timezone


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