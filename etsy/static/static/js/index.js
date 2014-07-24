$(document).ready(function() {
    var myApiKey = 'x24jerdzi236twww6lbcn5k5';
    var shopperID;

    $.ajax({
        url: 'https://openapi.etsy.com/v2/users/36147954.js?api_key=' + myApiKey,
        type: "GET",
        dataType: 'jsonp',
        success: function(response) {
            console.log(response);
            shopperID = response.results[0].user_id;
            console.log(shopperID);

        },
        error: function(response) {
            console.log(response);
        }
    });

});