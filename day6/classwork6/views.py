from django.shortcuts import render
from .models import Movie

def movie(request):

    if request.method == 'POST':

        name = request.POST.get('movie_name')
        year = request.POST.get('release_year')

        Movie.objects.create(
            movie_name=name,
            release_year=year
        )

        message = f"Movie saved: {name} ({year})"

        return render(request, 'classwork6/form-data.html', {
            'message': message
        })

    return render(request, 'classwork6/movie.html')