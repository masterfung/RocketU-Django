/**
 * Created by htm on 7/21/14.
 */

$.ajax({
        url: '/game/all_pokemon',
        type: "GET",
        success: function(data) {
            console.log(data);
        }
    });

var pokemonData = {
    pokedex_id: 25,
    image: "/media/img/25.png",
    name: "Pikachu",
    team: {
        type: "Random Team",
        id: 1
    }
};

pokemonData = JSON.stringify(pokemonData);
$.ajax({
    url: '/pokemon/new_pokemon/',
    type: 'POST',
    dataType: 'json',
    data: pokemonData,
    success: function(response) {
    },
    error: function(response) {
    }
});