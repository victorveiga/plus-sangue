from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Doador
from .forms import DoadorForm

# Create your views here.
@login_required
def store(request):
    doadores = Doador.objects.all()
    return render(request, 'list.html', {'doadores': doadores})

@login_required
def create(request):
    form = DoadorForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('doadores')    

    return render(request, 'form.html', {'form': form})  

@login_required
def update(request, id):
    doador = get_object_or_404(Doador, pk=id)
    form = DoadorForm(request.POST or None, request.FILES or None, instance=doador)

    if form.is_valid():
        form.save()
        return redirect('doadores')    

    return render(request, 'form.html', {'form': form})       