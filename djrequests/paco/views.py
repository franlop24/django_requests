from django.http import HttpResponse
from django.shortcuts import render

import requests

url = 'https://gateway.marvel.com:443/v1/public/'

apikey = 'aa91200d7881af0bf6252b6e99ef791e'

hash = '4cf11416913e6e7d3b7b87d59ae67423'

ts='1'

auth = f'?apikey={apikey}&ts={ts}&hash={hash}'

# Create your views here.
def index(request):
    url_full = f"{url}characters{auth}"
    response = requests.request('GET', url_full).json()

    return render(request,'paco/home.html', {'lista_heroes': response['data']['results']})

def get_character(request, id_character):
    url_full = f"{url}characters/{id_character}{auth}"
    response = requests.request('GET', url_full).json()

    return render(request,'paco/character.html', {
            'character': response['data']['results'][0]
        })