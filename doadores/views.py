from django.shortcuts import render, HttpResponse

# Create your views here.
def helloworld(request):
    return render(request, 'helloworld.html')