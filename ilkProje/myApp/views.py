from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hakkimizda(request):
    return render(request,'hakkimizda.html')

def iletisim(request):
    return render(request,"iletisim.html")