from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Movie

def home(request):

    query = request.GET.get('q', '')

    if query:
        movies = Movie.objects.filter(title__icontains=query).order_by('-date_added')
    else:
        movies = Movie.objects.all().order_by('-date_added')

    movies = Movie.objects.all().order_by('-date_added')

    return render(request, 'movies/home.html', {
        'movies': movies,
        'query': query
    })


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


def edit_movie(request):
    return render(request, "movie/add_movie.html")



def delete_movie(request):
    return render(request, "movie/home.html")

def toggle_watched(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    movie.is_watched = not movie.is_watched
    movie.save()
    return redirect('/')
    



    