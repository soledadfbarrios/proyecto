from django.shortcuts import render

# Create your views here.
def Home(request):
    #el aparametro cuando recibimos peticiones del navegador
    return render(request, 'libro/index.html')