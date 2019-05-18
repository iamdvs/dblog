from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.



class Post(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=1000)

    def slug(self):
        return slugify(self.title)


