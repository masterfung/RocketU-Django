import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from game.models import Pokemon, Team


def home(request):
    return render_to_response('base.html', locals(), context_instance=RequestContext(request))

@csrf_exempt
def all_pokemon(request):
    pokemon_objects = Pokemon.objects.all()
    collection = []
    for pokemon in pokemon_objects:
        collection.append({
            'name': pokemon.name,
            'image': pokemon.image,
            'pokedex_id': pokemon.pokedex_id,
            'id': pokemon.pk,
            'team': {
                'id': pokemon.team.id,
                'name': pokemon.team.name
            }
        })
    return HttpResponse(
                json.dumps(collection),
                content_type='application/json'
           )

@csrf_exempt
def new_pokemon(request):
    if request.method == 'POST':
        data = json.loads(request.body) #.loads is for json translation to python readable; .body is a django thing
        collection = []
        for pokemon in data['members']:
            new_pokemon = Pokemon.objects.create(
                name=pokemon['name'],
                image=pokemon['image'],
                pokedex_id=pokemon['pokedex_id'],
                team=Team.objects.get(id=data['team_info']['id'])
            )
            print new_pokemon
            collection.append({  #if there are a lot of pokemon then you will need a for loop
                'name': new_pokemon.name,
                'image': new_pokemon.image,
                'pokedex_id': new_pokemon.pokedex_id,
                'id': new_pokemon.pk,
                'team': {
                    'id': new_pokemon.team.id,
                    'name': new_pokemon.team.name
                }
            })

        return HttpResponse(json.dumps({'response': collection}),
                   content_type='application/json')

# from game.models import Team, Pokemon
# team = Team.objects.create(name='My team')
# pokemon = Pokemon.objects.create(name='Kingler',
#           pokedex_id = 99,
#           image='http://pokeapi.co//media/img/99.png',
#           team = team
#           )