from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import squirrel
from .forms import squirrelForm

def map(request):
    template = loader.get_template('maplot/map.html')
    return render(request, 'maplot/map.html', {})

def sightings(request):
    return HttpResponse("Hello, world. this is sightings page.")


def edit(request, Unique_Squirrel_ID):
    pet  = squirrel.object.get(id=Unique_Squirrel_ID)
    if request.method == 'POST':
	form = squirrelForm(request.POST, instance=pet)
	#checked data with form
	if form.is_valid():
	    form.save()
	    return redirect(f'/sightings/map/') #builds a redirect response y envia a otro url

    else:
	form = squirrelForm(instance = pet)
    context = { 'form' = form}
    return render(request, 'maplot/edit.html',context)

def add(request, Unique_Squirrel_ID):
    
    if request.method == 'POST':
        form = squirrelForm(request.POST)
        #checked data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/map/') #builds a redirect response y envia a otro url
    else:
        form = squirrelForm(instance = pet)
    context = { 'form' = form}
    return render(request, 'maplot/edit.html',context)
# Create your views here.
