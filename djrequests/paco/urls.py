from operator import imod
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('character/<int:id_character>/', views.get_character, name='character'),
]