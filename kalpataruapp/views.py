from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from kalpataruapp.models import Plant

# Create your views here.
def index(request):
    plants = Plant.objects.all()
    context = {
        'plants': plants
    }
    return render(request, 'kalpataruapp/index.html',context)

def search(request):        
    if request.method == 'GET':     
        plant_name =  request.GET.get('search')   
        plants = Plant.objects.all()
        print(plant_name)  
        try:
            status = Plant.objects.filter(name__icontains=plant_name) 
        except Plant.DoesNotExist:
            status = None
        return render(request,"kalpataruapp/search.html",{"names":status, 'plants': plants})
    else:
        return render(request,"kalpataruapp/search.html",{})
    
    