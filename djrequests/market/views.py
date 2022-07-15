import requests
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'market/index.html')

def form_token(request):
    return render(request, 'market/form_token.html')

def token(request):
    url = "https://franlopsmarket.herokuapp.com/franlops-market/api/auth/authenticate"

    payload = json.dumps({
    "username": request.POST['username'],
    "password": request.POST['password']
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return render(request, 'market/token.html', {'response': response.text})
    else:
        return render(request, 'market/token.html', {'response': "Error de Authentication"})

