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