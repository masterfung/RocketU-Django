import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from game.models import Pokemon, Team


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
                content_type='application.json'
           )

@csrf_exempt
def new_pokemon(request):
    if request.method == 'POST':
        data = json.loads(request.body) #.loads is for json translation to python readable; .body is a django thing
        pokemon = Pokemon.objects.create(
            name=data['name'],
            image=data['image'],
            pokedex_id=data['pokedex_id'],
            team=Team.objects.get(id=data['name'])
        )
        pokemon_info = {
            'name': pokemon.name,
            'image': pokemon.image,
            'pokedex_id': pokemon.pokedex_id,
            'team': {
                'id': pokemon.team.id,
                'type': pokemon.team.type
            }
        }
        return HttpResponse(json.dumps(pokemon_info),
                   content_type='application/json')

# from game.models import Team, Pokemon
# team = Team.objects.create(name='My team')
# pokemon = Pokemon.objects.create(name='Kingler',
#           pokedex_id = 99,
#           image='http://pokeapi.co//media/img/99.png',
#           team = team
#           )