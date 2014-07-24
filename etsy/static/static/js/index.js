$(document).ready(function() {
    var myApiKey = 'x24jerdzi236twww6lbcn5k5';
    var searchParameter;

    $.ajax({
        url: 'https://openapi.etsy.com/v2/listings/active.js?api_key=' + myApiKey,
        type: "GET",
        dataType: 'jsonp',
        success: function(response) {
            console.log(response);
            console.log(response.results[0].title);
            console.log(response.results[0].description);
//            shopperID = response.results[0].user_id;
//            console.log(shopperID);
            for (var i = 0; i < 5; i++) {
              $('.forSale').append(
                "<div><p>Item: <br>"+ response.results[i].title + "</p></div>" +
                "<div><p>Description: <br>"+ response.results[i].description + "</p></div>" +
                "<div><p>Url: <br><a href="+ response.results[i].url + ">Item Link</a></p></div>" +
                "<div><p>Price: $<br>"+ response.results[i].price + "</p></div>" +
                "<div><p>Quantity: <br>"+ response.results[i].quantity + "</p></div>" +
                "<hr/>"
            )
            }
        },
        error: function(response) {
            console.log(response);
        }
    }).complete(function () {

        $("#getShopBtn").on('click', function () {
            searchParameter = 'shops/TriforceInk';
        });

        $("#getUserBtn").on('click', function () {
            searchParameter = 26820281;
        });

        $("#getShopListings").on('click', function () {
            searchParameter = 'shops/TriforceInk/listings/active'
        });

        $("#searchBtn").on('click', function () {
            $.ajax({
            url: 'https://openapi.etsy.com/v2/'+ searchParameter +'.js?api_key=' + myApiKey,
            type: "GET",
            dataType: 'jsonp',
            success: function(response) {
                console.log(response.results[0]);
                $('.second').append(
                    "<div>"+ response + "</div>"
                )
            },
            error: function (response){
                console.log(response);
            }
            })
        })
    })

});