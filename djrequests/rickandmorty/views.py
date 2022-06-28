from django.http import HttpResponse
from django.shortcuts import render

import requests

# Create your views here.
def home(request, page=1):

    url = f"https://rickandmortyapi.com/api/character/?page={page}"

    #payload = {}
    #headers = {}

    response = requests.request("GET", url).json()

    info = response["info"]
    info['actual'] = page
    info['prev'] = page - 1 if page > 1 else None
    info['next'] = page + 1 if page < 42 else None
    
    characters = response['results']

    return render(request, 'rickandmorty/index.html', {
                                                    'info': info,
                                                    'characters': characters
                                                    })

def search(request):
    text_search = request.POST['text_search']
    
    url = f"https://rickandmortyapi.com/api/character/?name={text_search}"

    response = requests.request("GET", url).json()

    characters = response['results']

    return render(request, 'rickandmorty/search.html', {'characters': characters})
    
