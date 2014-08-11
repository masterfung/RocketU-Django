/**
 * Created by htm on 8/11/14.
 */
var rotten = angular.module('rottenApp', []);

rotten.factory('MovieApi', function () {
	return '88a8qpv9kwg657jxb97ma5nn';
});

rotten.controller('rottenCtrl', function ($scope, $http, MovieApi) {
	$scope.rottenList = [];
	$scope.rottenImage = [];
	$http.jsonp('http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters', {
		 params: {
		     apikey: MovieApi,
		     page_limit: '10',
		     callback: 'JSON_CALLBACK'
		 }
	}).then(function (promise) {
		console.log(promise);
		for (var i = 0; i < promise.data.movies.length; i++) {
	     $scope.rottenList.push(promise.data.movies[i]);
		 console.log(promise.data.movies[i].posters.profile);
		 var image = promise.data.movies[i].posters.profile;
		 var changeImage = image.replace('_tmb', '_det');
		 console.log(changeImage);
		 $scope.rottenImage.push(changeImage);
	 }
		console.log($scope.rottenList[1]);
		console.log($scope.rottenImage);
	})
});