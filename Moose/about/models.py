from django.db import models


# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=303)
    text = models.TextField()
    image = models.ImageField()
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=303)
    linkt = models.CharField(max_length=202)
    linkf = models.CharField(max_length=202)
    linki = models.CharField(max_length=204)

    def __str__(self):
        return self.title
