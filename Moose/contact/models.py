from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=202)
    phone = models.CharField(max_length=202)
    email = models.EmailField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ComtactMe(models.Model):
    icon = models.CharField(max_length=202)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.name
