from django.db import models

# Create your models here.

class blog(models.Model):

    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:200]

    def __str__(self):
        return "{}. {}".format(self.id,self.title)