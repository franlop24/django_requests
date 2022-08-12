from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.index, name='index'),
    path('ftoken/', views.form_token, name='form_token'),
    path('token/', views.token, name='token'),
    path('product/<int:productId>', views.product, name='product'),
    path('product/<int:productId>/delete', views.delete, name='delete'),
    path('product/nuevo', views.nuevo, name='nuevo'),
]