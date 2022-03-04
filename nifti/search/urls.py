# Import path for matching url patters to views.
from django.urls import path
# Import views.py from local directory.
from . import views

urlpatterns = [
  path('', views.search, name='search-home'),
]