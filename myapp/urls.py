from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,),
    path('drinks/<str:drink_name>', views.drinks),
    path('drinks/', views.drinks),
]