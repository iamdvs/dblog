from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from django.views.generic import TemplateView
from .models import *
from .forms import *

# index page 
def index(request):

    posts=Post.objects.all()

    return render(request,'blog/index.html',{'posts':posts})

#create post
def create_post(request):
    if request.method=='GET':   
        return render(request,'createPost.html')

    elif request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
                form.save()
                return redirect('/blog/')
    else:
        form=ImageForm()
    return render(request,'createPost.html')   

#post full views
def description(request,post_id):
    des = Post.objects.get(pk=post_id)
    return render(request,'blog/detail.html',{'des':des})
