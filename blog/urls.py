from django.urls import path
from . import views

# The structure of this module is based on the project urls.py file
# urlpattern is a list imported whre path is from django
# Note the name of the path: 2 terms

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]