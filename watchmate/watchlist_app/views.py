from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from .models import Movie
# Create your views here.


def movie_list(request):
    movies = Movie.objects.all()
    print(movies)
    data = {
        "movies":list(movies.values())
    }
    return JsonResponse(data)

def movie_detail(request, pk):
    movie_details = Movie.objects.get(pk=pk)
    print(movie_details)
    return HttpResponse(movie_details)