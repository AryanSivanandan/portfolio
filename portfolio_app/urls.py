from django.urls import path 
from .views import HomeView , contact_view

urlpatterns = [
    path('', HomeView.as_view() , name = 'home'),
    path('contact/' , contact_view , name = 'contact')
]