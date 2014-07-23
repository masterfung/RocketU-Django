/**
 * Created by htm on 7/23/14.
 */

$(document).ready(function() {
//    $.ajax({
//        url: 'http://api.rottentomatoes.com/api/public/v1.0/movies/769959054/similar.json?apikey=88a8qpv9kwg657jxb97ma5nn&limit=3',
//        type: 'GET',
//        dataType: 'jsonp',
//        success: function (response) {
//            console.log(response);
//        },
//        error: function (response) {
//            console.log(response);
//        }
//    }
    var myApiKey = 'y2fb7ajxwdkc8h8y22ur7eer';
    var movieID;



    $('.searchTinder').on('click', function() {

        var searchQuery = $('#favoriteMovie').val();
        var pageLimit = 3;

        $.ajax({
        url: 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=' + myApiKey + '&q=' + searchQuery + '&q=' + pageLimit,
        type: 'GET',
        dataType: 'jsonp',
        success: function (response) {
            console.log(response.movies[0].id);
            movieID = response.movies[0].id;
        },
        error: function (response) {
            console.log(response);
        }
    }).complete(function () {
            $.ajax({
                url: 'http://api.rottentomatoes.com/api/public/v1.0/movies/'+ movieID + '/similar.json?apikey=' + myApiKey +'&limit=5',
                type: 'GET',
                dataType: 'jsonp',
                success: function (response) {
                    console.log(response);
                    for (var i = 0; i < response.movies.length; i++) {
                        $('#recommended').append(
                            "<div>" +
                                "<p>" + response.movies[i].title +"</p>" +
                                "<p>" + response.movies[i].runtime +" mins</p>" +
                                "<p class='hidden>" + response.movies[i].synopsis +" mins</p>" +
                                "<p> Year: " + response.movies[i].year +"</p>" +
                                "<button class='learnMore'>Favorite</button>" +
                                "<button class='favorite'>Favorite</button>" +
                                "<button class='favorite'>Favorite</button>" +
                            "</div>"
                        )
                    }
                },
                error: function (response) {
                    console.log(response);
                }
            })
        })
});

    $(document).on('click', '.learn', function () {
        $.ajax({
            url: 'http://api.rottentomatoes.com/api/public/v1.0/movies/'+ movieID + '/similar.json?apikey=' + myApiKey +'&limit=5',
                type: 'GET',
                dataType: 'jsonp',
                success: function (response) {
                    console.log(response);
//                    $('.learnMore').on('click', function () {
//                        $(this).toggle();
//                    })
                },
                error: function (response) {
                    console.log(response);
                }
            })
        })
    });

