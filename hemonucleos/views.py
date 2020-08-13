from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Hemonucleo
from .forms import HemonucleoForm

# Create your views here.
@login_required
def store(request):
    hemonucleos = Hemonucleo.objects.all()
    return render(request, 'hemonucleo_list.html', {'hemonucleos': hemonucleos})

@login_required
def create(request):
    form = HemonucleoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('hemonucleos')    

    return render(request, 'hemonucleo_form.html', {'form': form})  

@login_required
def update(request, id):
    hemonucleo = get_object_or_404(Hemonucleo, pk=id)
    form = HemonucleoForm(request.POST or None, request.FILES or None, instance=hemonucleo)

    if form.is_valid():
        form.save()
        return redirect('hemonucleos')    

    return render(request, 'hemonucleo_form.html', {'form': form})       