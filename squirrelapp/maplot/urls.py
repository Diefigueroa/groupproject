from django.urls import path

from . import views

urlpatterns = [
    path('', views.sightings, name='sightings'),
    path('<int:squirrel_id>', views.update_delete, name='update_delete'),
    path('add', views.add, name='add'),
]
