from django.shortcuts import render

# Create your views here.

def to_do(request):
    return render(request,template_name="to-do/to_do.html")