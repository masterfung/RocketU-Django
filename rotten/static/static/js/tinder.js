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
    var movieInfo = {};


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
                    var movies = response.movies;
                    movieList = [];
                    for (i = 0; i < movies.length; i++) {
                        movieInfo = {};
                        movie = movies[i];
                        movieInfo.title = movie.title;
                        movieInfo.release_year = movie.year;
                        movieInfo.critics_score = movie.ratings.critics_score;
                        movieInfo.poster = movie.posters.original;
                        movieInfo.mpaa_rating = movie.mpaa_rating;
                        movieInfo.runtime = movie.runtime;
                        movieInfo.audience_score = movie.ratings.audience_score;
                        movieList.push(movieInfo);


                        $('#recommended').append(
                            "<div>" +
                                "<p>" + response.movies[i].title +"</p>" +
                                "<p>" + response.movies[i].runtime +" mins</p>" +
                                "<p class='hidden'>MPAA Ratings: " + response.movies[i].mpaa_rating +"</p>" +
                                "<img src="+response.movies[i].posters.original+">" +
                                "<p> Year: " + response.movies[i].year +"</p>" +

                                "<button class='learnMore'>Learn More</button>" +
                                "</p><button class='favorite' data-id="+i+">Favorite This Movie</button></p>" +
                            "</div>"
                        )

                    }

                },
                error: function(response) {
                    console.log(response);
                }

        })
});

    $(document).on('click', '.learnMore', function () {
        $('.hidden').toggle();

        })
    });

    $(document).on('click', '.favorite', function () {
        var referencial = $(this).data('id');
        var movieInfo = movieList[referencial];
        $(this).html("<img src='http://newsupermariobros2.nintendo.com/mobile/_ui/img/power-ups/carousel/super-star.png' width=50>");
        movieInfo = JSON.stringify(movieInfo);
        $.ajax({
            url: '/new_tinder_html/',
            type: 'POST',
            dataType: 'html',
            data: movieInfo,
            success: function(movie_response) {
                console.log(movie_response);
            },
            error: function(error_response) {
                console.log(error_response);
            }
        });
    });
    $('#getAllFavorites').on('click', function() {
        $.ajax({
            url: '/all_favorites/',
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                console.log(response);
                console.log(response[0].audience_score);
                for (var j = 0; j < response.length; j++) {
                    $(".favorites").append(
                            "<div>Title: "+ response[j].title +"</div>" +
                            "<div>Year: "+ response[j].release_year +"</div>" +
                            "<div>Critics Score: "+ response[j].critics_score +"</div>" +
                            "<div>Poster: <img src="+ response[j].poster +"></div>" +
                            "<div>MPAA Rating: "+ response[j].mpaa_rating +"</div>" +
                            "<div>Audience Score: "+ response[j].audience_score +"</div>" +
                            "<hr>"
                    )
                }
            },
            error: function(response) {
                console.log(response);
            }
        });
    });
    });
