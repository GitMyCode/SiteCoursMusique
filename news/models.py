from django.db import models

class New(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField('date published')

    def __unicode__(self):
       return self.title


class Comment(models.Model):
   new = models.ForeignKey(New)
   author = models.CharField(max_length=60)
   creation_date = models.DateTimeField('date published')
   comment = models.TextField()

   def __unicode__(self):
      return self.author + self.comment[:10]