from django.shortcuts import render

def index(request):
    return render(request, 'tripapp/index.html')

def about(request):
    return render(request, 'tripapp/about.html')

def login(request):
    return render(request, 'tripapp/login.html')

def weather(request):
    return render(request, 'tripapp/weather.html')

def profile(request):
    return render(request, 'tripapp/profile.html')

def myposts(request):
    return render(request, 'tripapp/myposts.html')

def messages(request):
    return render(request, 'tripapp/messages.html')

def explore(request):
    return render(request, 'tripapp/explore.html')

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests

YOUTUBE_API_KEY = 'AIzaSyDbSCu3VjTPVTS89Nz0K-fK7Jn4SLcUc1o'
# this is full
# new one
# YOUTUBE_API_KEY = 'AIzaSyDCVUfD2upIH9UJtTRgvi-Ufpll603WF4w'

@require_http_methods(["GET"])
def search_youtube_for_city(request):
    city_name = request.GET.get('city', '')
    max_results = 1
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part': 'snippet',
        'q': city_name,
        'type': 'video',
        'key': YOUTUBE_API_KEY,
        'maxResults': max_results
    }
    response = requests.get(search_url, params)
    # debugging statements
    print(response.text)
    videos = response.json().get('items', [])
    return JsonResponse({'videos': videos})  # Wrap the YouTube response in a dictionary under the 'videos' key