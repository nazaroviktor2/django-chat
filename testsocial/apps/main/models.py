from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):
    message = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("text")
    pub_data = models.DateTimeField("publication date")

    def __str__(self):
        return self.text
