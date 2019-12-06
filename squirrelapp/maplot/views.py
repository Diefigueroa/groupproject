from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def map(request):
    template = loader.get_template('maplot/map.html')
    return render(request, 'maplot/map.html', {})

def sightings(request):
    return HttpResponse("Hello, world. this is sightings page.")

def update_delete(request):
    return HttpResponse("Hello, world. this is update/delete page.")

def add(request):
    return HttpResponse("Hello, world. this is add page.")
# Create your views here.
