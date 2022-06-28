from operator import imod
from django.urls import path

from . import views

urlpatterns = [
    path('characters/', views.home, name='home'),
    path('characters/<int:page>', views.home, name='home'),
    path('characters/search', views.search, name='search'),
]