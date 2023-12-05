from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    context = {
        'urunlerim':urunler
    }
    return render(request,"index.html",context)