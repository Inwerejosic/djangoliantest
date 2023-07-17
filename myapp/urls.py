from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,),
    path('about', views.about,),
    path('menu', views.menu,),
    path('book', views.book, name='book'),
    path('modify_str', views.modify_str, name='modify_str'),
    path('drinks/<str:drink_name>', views.drinks),
    path('drinks/', views.drinks),
]