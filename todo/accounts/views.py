from django.shortcuts import render

def login(request):
    return render(request, template_name="registration/login.html")

def register(request):
    return render(request, template_name="registration/register.html")