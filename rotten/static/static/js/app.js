/**
 * Created by htm on 8/11/14.
 */
var rotten = angular.module('rottenApp', []);

rotten.factory('MovieApi', function () {
	return '88a8qpv9kwg657jxb97ma5nn';
});

rotten.controller('upcomingCtrl', function ($scope, $http, MovieApi) {
	$scope.rottenList = [];
	$scope.rottenImage = [];
	$http.jsonp('http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters', {
		 params: {
		     apikey: MovieApi,
		     page_limit: '10',
		     callback: 'JSON_CALLBACK'
		 }
	}).then(function (promise) {
		for (var i = 0; i < promise.data.movies.length; i++) {
	     $scope.rottenList.push(promise.data.movies[i]);
		 var image = promise.data.movies[i].posters.profile;
		 var changeImage = image.replace('_tmb', '_det');
		 $scope.rottenImage.push(changeImage);
	 }
	})
});

rotten.controller('movieCtrl', function ($scope, $http) {
	$scope.titles = [];
	$scope.retrieveMovies = function () {
		$http.jsonp(
		 'http://api.rottentomatoes.com/api/public/v1.0/movies', {
				params: {
					apikey: '88a8qpv9kwg657jxb97ma5nn',
					q: $scope.movies,
					page_limit: '10',
					callback: 'JSON_CALLBACK'
				}
			}).then(function (promise) {
				console.log(promise.data.movies);
				for (var i = 0; i < promise.data.movies.length; i++) {
					$scope.titles.push(promise.data.movies[i]);
				}
				$scope.showResults = true;

			}
		);
	};
	$scope.showMovieInfo = function() {
		$scope.movieDescription = $scope.movieDescription ===  false ? true: false;
	};

});