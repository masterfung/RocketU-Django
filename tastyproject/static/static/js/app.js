/**
 * Created by htm on 8/12/14.
 */

var app = angular.module('myApp', [
	'ngRoute',
	'ngResource'
]);

app.config(function ($routeProvider) {
	$routeProvider
		.when('/', {
			templateUrl: '../static/views/index.html',
			controller: 'indexCtrl'
		})
});