from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),     
    path('map/', views.map, name='map'),
    path('sightings/stats/', views.squirrel_stats,name='stats'),
    path('sightings/<str:Unique_Squirrel_ID>/', views.edit, name='edit'),
    path('sightings/add/', views.add, name='add'),
    
]
