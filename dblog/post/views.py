from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from django.views.generic import TemplateView
from .models import Post

# Create your views here.

def index(request):

    posts=Post.objects.all()

    return render(request,'index.html',{'posts':posts})



def create_post(request):

    if request.method=='GET':   
        return render(request,'createPost.html')
    elif request.method=='POST':
        titlef=request.POST.get('title')
        descriptionf=request.POST.get('description')
        p=Post(title=titlef,description=descriptionf)
        p.save()

        return redirect('/')


def description(request,post_id):
    des = Post.objects.get(pk=post_id)
    return render(request,'detail.html',{'des':des})

    