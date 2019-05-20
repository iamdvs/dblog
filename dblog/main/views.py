from django.shortcuts import render,HttpResponse

# Create your views here.


def main(request):
    if request.method=='GET':
        return render(request,'main/main.html')
