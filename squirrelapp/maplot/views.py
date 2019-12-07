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
    squirrel_stats2=squirrel.objects.filter(Age='Juvenile').count()
    squirrel_stats3=squirrel.objects.filter(Running='true').count()
    squirrel_stats4=squirrel.objects.filter(Moans='true').count()
    squirrel_stats5=squirrel.objects.filter(Indifferent='true').count()
    context={'squirrel_stats1':squirrel_stats1,
            'squirrel_stats2':squirrel_stats2,
            'squirrel_stats3':squirrel_stats3,
            'squirrel_stats3':squirrel_stats3,
            'squirrel_stats4':squirrel_stats4,
            'squirrel_stats5':squirrel_stats5,
            }
    return render(request, 'maplot/stats.html', context)

def map(request):
    sightings = squirrel.objects.all()
    form = QueryForm(request.GET or None)
    paramDict = request.GET

    books = filter_books(books, paramDict)

    page_count = books.aggregate(Sum('pages'))
 
    map_books = [{'loc':[float(book.Longitude), float(book.Latitude)], 
                  'title':book.Unique_Squirrel_ID,
                  'url':book.get_absolute_url()} for book in books]
    context = {
        'sightings':sightings,
        # Here, we apply `json.dumps`, `escapejs` and `marksafe` for security 
        # and proper formatting
        'map_books': mark_safe(escapejs(json.dumps(map_books))),
        'page_count':page_count['pages__sum'], 
        'form':form}

    return render(request, 'maplot/map.html', context)



def sightings(request):
    return HttpResponse("Hello, world. this is sightings page.")

def stats(request):
    return HttpResponse("Hello, world. this is sightings page.")

def edit(request, Unique_Squirrel_ID):
    pet  = squirrel.objects.get(pk =Unique_Squirrel_ID)
    if request.method == 'POST':
        form = squirrelForm(request.POST,instance=pet)
    
        if form.is_valid():
            form.save()
            return redirect(f'/maplot/map/')

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
            return redirect(f'/maplot/map/') 
    else:
        form = squirrelForm()
    context = {
            'form':form,
            }
    return render(request, 'maplot/edit.html',context)
