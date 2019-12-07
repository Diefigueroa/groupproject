from django.urls import path

from . import views

urlpatterns = [

    path('map/', views.map, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/<int:Unique_Squirrel_ID>/', views.edit, name='edit'),
    path('sightings/add/', views.add, name='add'),

    
]
