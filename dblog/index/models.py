from django.db import models
from django.template.defaultfilters import slugify
import jdatetime
from django import forms


class Post(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=1000)
    created_at=jdatetime.datetime.now().strftime("%y,%m,%d").replace(',','/')
    image=models.ImageField(upload_to='images/',default = 'None/no-img.jpg',blank=True)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title    




