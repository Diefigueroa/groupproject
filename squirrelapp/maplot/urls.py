from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),     
    path('map/', views.map, name='map'),
    path('stats/', views.squirrel_stats,name='stats'),
    path('add/', views.add, name='add'),
    path('str:Unique_Squirrel_ID>/', views.edit, name='edit'),
    path('<str:Unique_Squirrel_ID>/details', views.details, name='details'),
    
    
]
