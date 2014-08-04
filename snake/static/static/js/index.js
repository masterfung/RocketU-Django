/**
 * Created by htm on 8/4/14.
 */
$(document).ready(function () {
	$.ajax({
		url:"/score_return",
		type: 'GET',
		success: function(score){
			console.log(score);

		},
		error: function(score) {
			console.log(score);
		}
	})

});