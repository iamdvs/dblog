from django.shortcuts import render,HttpResponse
from django.template import loader
from django.views.generic import TemplateView
# Create your views here.

def index(request):

    return render(request,'index.html')


# class HomePageView(TemplateView):
#     template_name = "index.html"



