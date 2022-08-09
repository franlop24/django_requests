import requests
import json
import os

from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):

    token = os.environ.get('TOKEN')
    print(token)

    url = "https://franlopsmarket.herokuapp.com/franlops-market/api/products/all"

    payload={}
    headers = {
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    products = response.json()

    return render(request, 'market/index.html', {'products': products})

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
        os.environ['TOKEN'] = response.json()['jwt']
        return redirect('/market/products/')
    else:
        return render(request, 'market/token.html', {'response': "Error de Authentication"})

def product(request, productId):
    url = f"https://franlopsmarket.herokuapp.com/franlops-market/api/products/{productId}"

    payload={}

    token = os.environ.get('TOKEN')
    
    headers = {
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    product = response.json()

    return render(request, 'market/product.html', {'product': product})