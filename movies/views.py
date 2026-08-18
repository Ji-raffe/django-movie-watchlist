from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie

def home(request):
    return render(request, 'movies/home.html')


def add_movie(request):
    
    if request.method == "POST":
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        release_year = request.POST.get('release_year')
        personal_rating = request.POST.get('personal_rating')
        is_watched = request.POST.get('is_watched')

        if release_year:
            release_year = int(release_year)
        else:
            release_year = None

        if personal_rating:
            personal_rating = int(personal_rating)
        else:
            personal_rating = None

        if is_watched:
            is_watched = (is_watched == 'True')
        else:
            is_watched = False

        Movie.objects.create(
            title=title,
            genre=genre,
            release_year=release_year,
            personal_rating=personal_rating,
            is_watched=is_watched,
        )

        return redirect('/')
    
    return render(request, 'movies/add_movies.html')