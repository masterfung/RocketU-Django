/**
 * Created by htm on 7/21/14.
 */

$.ajax({
        url: '/all_pokemon',
        type: "GET",
        success: function(data) {
            console.log(data);
        }
    });

//var pokemonData = {
//    pokedex_id: 25,
//    image: "/media/img/25.png",
//    name: "Pikachu",
//    team: {
//        type: "Random Team",
//        id: 1
//    }
//};
//pokemonData = JSON.stringify(pokemonData);
//$.ajax({
//        url: '/new_pokemon/',
//        type: "POST",
//        dataType: "json",
//        data: pokemonData,
//        success: function(data) {
//            console.log(data);
//        }
//    });

$(document).ready(function(){

    var team = {};
    team.members = [];
    team.team_info = {name: "My Team", id: 1};
    $('.generate').on('click', function() {
        var random = Math.floor(Math.random() * (720) + 2);
        $.ajax({
                url: "http://pokeapi.co/api/v1/sprite/" + random + "/",
                type: "GET",
                dataType: "jsonp",
                success: function(data) {
                    var newPokemon = {};
                    newPokemon.name = data.name;
                    newPokemon.pokedex_id = data.id - 1;
                    newPokemon.image = data.image;
                    team.members.push(newPokemon);
//                    console.log(team.length);
//                    console.log(pokemon);

                var spriteUrl = 'http://pokeapi.co' + newPokemon.image;

                $('.pokemon')
                .append("<div class='pokebox'><div class='selection inactive'><img src=" + spriteUrl + "/>" +
                    "<p class='name'>" + newPokemon.name.charAt(0).toUpperCase() + newPokemon.name.substr(1).toLowerCase() + "</p></div></div>");
//                .append("<div class='pokebox'><div class='field inactive'><img src=" + spriteUrl + "/>" +
//                    "<p class='name'>" + pokemon.name.charAt(0).toUpperCase() + pokemon.name.substr(1).toLowerCase() + "</p></div></div>");

            },
            error: function(response) {
//                console.log(response);
            }
        });
    });

    $('.save').on('click', function() {
        console.log(team);
        team = JSON.stringify(team);
        $.ajax({
                url: '/new_pokemon/',
                type: "POST",
                dataType: "json",
                data: team,
                success: function(data) {
//                    console.log(data);
                },
                error:function(data) {
                    console.log(data);
                }

        })
    });
});