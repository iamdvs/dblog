from django.db import models
from django.template.defaultfilters import slugify
import jdatetime
from django import forms


class Post(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=300)
    text1=models.TextField(max_length=4000)
    image1=models.ImageField(upload_to='images/',default = 'None/no-img.jpg',blank=True)
    text2=models.TextField(max_length=10000)
    image2=models.ImageField(upload_to='images/',default = 'None/no-img.jpg',blank=True)
    text3=models.TextField(max_length=10000)
    image3=models.ImageField(upload_to='images/',default = 'None/no-img.jpg',blank=True)
    text4=models.TextField(max_length=10000)
    created_at=jdatetime.datetime.now().strftime("%y,%m,%d").replace(',','/')
    image=models.ImageField(upload_to='images/',default = 'None/no-img.jpg',blank=True)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title    




