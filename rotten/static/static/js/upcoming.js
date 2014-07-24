/**
 * Created by htm on 7/24/14.
 */

$(document).ready(function () {
    var myApiKey = 'y2fb7ajxwdkc8h8y22ur7eer';

    var selection = function (response) {
      for (var i = 0; i < response.movies.length; i++) {
                movies = response.movies[i];
                $('.upcoming').append(
                    "<div><img src=" + movies.posters.original + "></div>"+
                    "<div><h2>" + movies.title + "</h2></div>"+
                    "<div><p>MPAA Ratings: " + movies.mpaa_rating + "</p></div>"+
                    "<div><p>Audience Score: " + movies.ratings.audience_score + "</p></div>"+
                    "<div><p>Critics Score: " + movies.ratings.critics_score + "</p></div>"+
                    "<div><p>Critics Year: " + movies.year + "</p></div>"+
                    "<br>"
                )
            }
    };

    $('#playingNow').on('click', function(){
        $.ajax({
        url: 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=' + myApiKey,
        type: "GET",
        dataType: "jsonp",
        success: function (response) {
            console.log(response);
            selection(response);
        },
        error: function (response) {
            console.log(response);
        }
    })
    });

    $('#comingSoon').on('click', function(){
        $.ajax({
            url: 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json?apikey=' + myApiKey,
            type: "GET",
            dataType: "jsonp",
            success: function (response) {
                selection(response);
            }
        })
    });

    $('#myWatchlist').on('click', function(){

    });


});