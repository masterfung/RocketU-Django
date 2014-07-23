import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from tomatoes.models import Movie


def home(request):
    return render(request, 'tomatoes_base.html')

def all_favorites(request):
    all_movies = Movie.objects.all()
    return render_to_response('movie_template.html', all_movies)

@csrf_exempt
def new_movie_json(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        collection = []

        new_movie = Movie.objects.create(
            title=data['title'],
            release_year=data['release_year'],
            critics_score=data['critics_score'],
            poster=data['poster'],
            mpaa_rating=data['mpaa_rating'],
            runtime=data['runtime'],
            audience_score=data['audience_score'],
        )
        print new_movie
        collection.append({
            'title': new_movie.title,
            'release_year': new_movie.release_year,
            'critics_score': new_movie.critics_score,
            'poster': new_movie.poster,
            'mpaa_rating': new_movie.mpaa_rating,
            'runtime': new_movie.runtime,
            'audience_score': new_movie.audience_score,
        })
        return HttpResponse(json.dumps({'response': collection}), content_type='application/json')

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