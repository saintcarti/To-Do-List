from django.urls import path

from . import views

urlpatterns = [
    path('to-do/', views.to_do, name="to_do"),
]