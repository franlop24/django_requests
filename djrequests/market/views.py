from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'market/index.html')

def form_token(request):
    return render(request, 'market/form_token.html')

def token(request):
    return render(request, 'market/token.html')