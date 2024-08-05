from django.shortcuts import render

# Create your views here.

def base(request):
    
    return render(request,template_name="base.html")


def index(request):
    return render(request,template_name="index.html")