from django.urls import path

from myproject.first_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
