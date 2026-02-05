from django.shortcuts import render
from .models import Movie

def home(request):
    movies = Movie.objects.all()
    return render(request, 'movie/home.html', {'movies': movies})

def about(request):
    return render(request, 'movie/about.html')
