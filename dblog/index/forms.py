from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','description','image']