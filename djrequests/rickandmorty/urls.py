from operator import imod
from django.urls import path

from . import views

urlpatterns = [
    path('characters/<int:page>', views.home, name='home'),
]