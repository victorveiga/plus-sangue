from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from doadores.forms import DoadorForm
from hemonucleos.forms import HemonucleoForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        form_doador = DoadorForm(request.POST or None, request.FILES or None)
        form_hemocentro = HemonucleoForm(request.POST or None, request.FILES or None)

        if form_doador.is_valid():
            form_doador.save()

        if form_hemocentro.is_valid():
            form_hemocentro.save()    

        return render(request, 'index.html', {'form_doador': form_doador, 'form_hemocentro': form_hemocentro})    