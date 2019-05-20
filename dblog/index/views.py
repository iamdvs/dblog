from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from django.views.generic import TemplateView
from .models import *
from .forms import *

# index page 
def index(request):

    posts=Post.objects.all()

    return render(request,'index.html',{'posts':posts})

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
    return render(request,'detail.html',{'des':des})


#manage for posts
def manage(request):
    if request.method == 'GET':
        posts=Post.objects.all()
        return render(request,'manage.html',{'posts':posts})   
      
def manageDelete(request,post_id):
    if request.method == 'POST':
        Post.objects.filter(id=post_id).delete()
        return redirect('/blog/manage/')

#edit post 
def editPost(request,post_id):
    if request.method == "GET":
        information=Post.objects.get(pk=post_id)
        return render(request,'editPost.html',{'information':information})

    elif request.method == "POST":
            mypost=Post.objects.get(id=post_id)

            mypost.title=request.POST.get('Etitle')
            mypost.description=request.POST.get('Edescription')
            mypost.save()
            
            return redirect('/blog/manage/')