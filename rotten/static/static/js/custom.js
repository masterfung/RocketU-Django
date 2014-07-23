$(document).ready(function() {
    var myApiKey = 'y2fb7ajxwdkc8h8y22ur7eer';
    var searchQuery;
    var pageLimit = 10;
    var movieInfo = {};

    $(document).on('click', '#searchBtn', function() {
        var reference = [];
        searchQuery = $('#search').val();
        console.log(searchQuery);
//        $('.getMovie').on('click', function() {
        $.ajax({
        url: 'http://api.rottentomatoes.com/api/public/v1.0/' +
          'movies.json?apikey=' + myApiKey + '&q=' +
           searchQuery + '&page_limit=' + pageLimit,
        type: 'GET',
        dataType: 'jsonp',
        success: function(movie_response) {
            console.log(movie_response);
            var movies = movie_response.movies;
            var movieList = [];
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
                console.log(movieInfo);

                $('.movieInfoContainer').append(
                    "<div class='movieItem'><img class='moviePoster'src="+movieInfo.poster+
                        "><p class='movieTitle'>"+movieInfo.title+
                        "</p><p class='movieScore'>Movie Score: "+movieInfo.critics_score+
                        "</p><button class='favorite' data-id="+i+">Favorite This Movie</button></p><button class='moreInfoBtn'>More Information</button>" +
                        "<div class='moreInfo' style='display:none;'><p class='mpaaRating'>MPAA Rating: "+movieInfo.mpaa_rating+
                        "</p><p class='runtime'>Runtime: "+movieInfo.runtime+"</p></div></div>"
                )
                console.log(reference);
            }
            $('.favorite').on('click', function () {
                var referencial = $(this).data('id');
                var movieInfo = movieList[referencial];
                $(this).html("<img src='http://newsupermariobros2.nintendo.com/mobile/_ui/img/power-ups/carousel/super-star.png' width=50>");
                movieInfo = JSON.stringify(movieInfo);
                $.ajax({
                    url: '/new_movie_html/',
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

            $('.moreInfoBtn').on('click', function () {
                    console.log('More Information Coming');
                    $(this).text(function (i, text) {
                        return text === "More Information" ? "Less Information" : "More Information";
                    });
                    $(this).siblings('.moreInfo').toggle()
                });
        },
        error: function(error_response) {
            console.log(error_response);

        }
    })
    });



    $('.saveMovie').on('click', function() {
    movieInfo = JSON.stringify(movieInfo);
    $.ajax({
        url: '/new_movie_json/',
        type: 'POST',
        dataType: 'json',
        data: movieInfo,
        success: function(movie_response) {
            console.log(movie_response);
        },
        error: function(error_response) {
            console.log(error_response);
        }
    });
});

//    movieInfo = JSON.stringify(movieInfo);
//    $.ajax({
//        url: '/new_movie_html/',
//        type: 'POST',
//        dataType: 'html',
//        data: movieInfo,
//        success: function(movie_response) {
//            console.log(movie_response);
//        },
//        error: function(error_response) {
//            console.log(error_response);
//        }
//    });

    $('.saveMovieHtml').on('click', function() {
    movieInfo = JSON.stringify(movieInfo);
    $.ajax({
        url: '/new_movie_html/',
        type: 'POST',
        dataType: 'html',
        data: movieInfo,
        success: function(movie_response) {
            console.log(movie_response);
            $('.movieInfoContainer').html(movie_response);
        },
        error: function(error_response) {
            console.log(error_response);
        }
    });
});



});