/**
 * Created by htm on 8/10/14.
 */
var etsy = angular.module('etsyApp', []);

etsy.controller('etsyCtrl', function ($scope, $http) {
	$scope.etsySelection = [];
	$scope.api_key = "x24jerdzi236twww6lbcn5k5";
	$scope.retrieveList = function() {
		$http.jsonp (
			"https://openapi.etsy.com/v2/shops/TriforceInk/listings/active.js?api_key=" + $scope.api_key, {
				params: {
					callback: 'JSON_CALLBACK'
				}
			}).then(function (promise) {
				console.log(promise.data.results[0].description);
				for (var i = 0; i < promise.data.results.length; i++) {
					$scope.etsySelection.push(promise.data.results[i]);
				}
				console.log($scope.etsySelection);
				console.log(promise.data.results.length);
			});

	};

});