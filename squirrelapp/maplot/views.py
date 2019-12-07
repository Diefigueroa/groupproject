from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import squirrel
from django import forms
from .forms import squirrelForm

def index(request):
    squirrels = squirrel.objects.all()
    fields = ['Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age','Primary_fur_color','Location','Specific_location','Running','Chasing','Climbing','Eating','Foraging','Other_Activities','Kuks','Quaas','Moans','Tail_Flags','Tail_Twitches','Approaches','Indifferent','Runs_From']
    context={
            'squirrels':squirrels,
            'fields':fields,
            }
    return render(request,'maplot/all.html',context)

def squirrel_stats(request):
    squirrel_stats1=squirrel.objects.all().count()
    squirrel_stats2=squirrel.objects.filter(Age=='Juvenile').count()
    squirrel_stats3=squirrel.objects.filter(Running=='True').count()
    squirrel_stats4=squirrel.objects.filter(Moans=='True').count()
    squirrel_stats5=squirrel.objects.filter(Indifferent=='True').count()
    context={'squirrel_stats1':squirrel_stats1,
            'squirrel_stats2':squirrel_stats2,
            'squirrel_stats3':squirrel_stats3,
            'squirrel_stats3':squirrel_stats3,
            'squirrel_stats4':squirrel_stats4,
            'squirrel_stats5':squirrel_stats5,
            }
    return render(request, 'maplot/stats.html', context)

def map(request):
    template = loader.get_template('maplot/map.html')
    return render(request, 'maplot/map.html', {})

def sightings(request):
    return HttpResponse("Hello, world. this is sightings page.")


def edit(request, Unique_Squirrel_ID):
    pet  = squirrel.object.get(id=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = squirrelForm(request.POST,instance=pet)
    
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/map/')

    else:
        form = squirrelForm(instance=pet)
        context = {
                'form':form,
                }
    return render(request, 'maplot/edit.html',context)

def add(request):
    
    if request.method == 'POST':
        form = squirrelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/map/') 
    else:
        form = squirrelForm()
        context = {
                'form':form,
                }
    return render(request, 'maplot/edit.html',context)
