from django.shortcuts import render
from deneme.models import DenemeModel

def denemeListe(request):
    gonderiler = DenemeModel.objects.all()
    return render(request,'deneme/liste.html',{"gonderis": gonderiler})
