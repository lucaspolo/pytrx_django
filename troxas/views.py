from django.shortcuts import render
from .models import Troxa

# Create your views here.
def troxa_listar(request):
    troxas = Troxa.objects.all()
    return render(request, 'troxas_listar.html', {'troxas': troxas})
