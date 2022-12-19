from django.db import models


# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=404)
    content = models.TextField()
    image = models.ImageField()
    name = models.CharField(max_length=202)
    about = models.CharField(max_length=303)



    def __str__(self):
        return self.title
