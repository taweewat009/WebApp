from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def certificate(request):
    return render(request, 'certificate.html')
