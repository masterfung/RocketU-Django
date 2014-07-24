import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from tomatoes.models import Movie


def home(request):
    favorites = Movie.objects.all()
    data = {'favorites': favorites}
    return render(request, 'tomatoes_base.html', data)

def tinder(request):
    # favorites = Movie.objects.all()
    # source = {'favorites': favorites}
    return render(request, 'tinder.html')

def upcoming(request):
    return render(request, 'upcoming.html')
#
# @csrf_exempt
# def new_movie_json(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         collection = []
#
#         new_movie = Movie.objects.create(
#             title=data['title'],
#             release_year=data['release_year'],
#             critics_score=data['critics_score'],
#             poster=data['poster'],
#             mpaa_rating=data['mpaa_rating'],
#             runtime=data['runtime'],
#             audience_score=data['audience_score'],
#         )
#         print new_movie
#         collection.append({
#             'title': new_movie.title,
#             'release_year': new_movie.release_year,
#             'critics_score': new_movie.critics_score,
#             'poster': new_movie.poster,
#             'mpaa_rating': new_movie.mpaa_rating,
#             'runtime': new_movie.runtime,
#             'audience_score': new_movie.audience_score,
#         })
#         return HttpResponse(json.dumps({'response': collection}), content_type='application/json')

@csrf_exempt
def new_movie_html(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_movie = Movie.objects.create(
            title=data['title'],
            release_year=data['release_year'],
            critics_score=data['critics_score'],
            poster=data['poster'],
            mpaa_rating=data['mpaa_rating'],
            runtime=data['runtime'],
            audience_score=data['audience_score'],
        )
        movie_info = {
            'title': new_movie.title,
            'release_year': new_movie.release_year,
            'critics_score': new_movie.critics_score,
            'poster': new_movie.poster,
            'mpaa_rating': new_movie.mpaa_rating,
            'runtime': new_movie.runtime,
            'audience_score': new_movie.audience_score,
        }
        return render_to_response('movie_template.html', movie_info)


@csrf_exempt
def new_tinder_html(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_movie = Movie.objects.create(
            title=data['title'],
            release_year=data['release_year'],
            critics_score=data['critics_score'],
            poster=data['poster'],
            mpaa_rating=data['mpaa_rating'],
            runtime=data['runtime'],
            audience_score=data['audience_score'],
        )
        movie_info = {
            'title': new_movie.title,
            'release_year': new_movie.release_year,
            'critics_score': new_movie.critics_score,
            'poster': new_movie.poster,
            'mpaa_rating': new_movie.mpaa_rating,
            'runtime': new_movie.runtime,
            'audience_score': new_movie.audience_score,
        }
        return render_to_response('tinder.html', movie_info)

@csrf_exempt
def all_favorites(request):
    movies = Movie.objects.all()

    favorites_array = []
    for favorite in movies:
        favorites_array.append({
            'title': favorite.title,
            'release_year': favorite.release_year,
            'critics_score': favorite.critics_score,
            'poster': favorite.poster,
            'mpaa_rating': favorite.mpaa_rating,
            'runtime': favorite.runtime,
            'audience_score': favorite.audience_score,
        })
    return HttpResponse(json.dumps(favorites_array), content_type='application/json')