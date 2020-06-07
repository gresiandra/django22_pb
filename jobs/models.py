from django.db import models

# Create your models here.

class job(models.Model):
    
    image = models.ImageField(upload_to='')
    summary = models.CharField(max_length=200)


def __str__(self):
    return "{}. {}".format(self.id, self.summary)
