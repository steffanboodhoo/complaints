angular.module('complaints')

.controller('formCtrl',['$scope',function($scope){
	$scope.teams = [
		{'name':'Software Dev','id':1},
		{'name':'Products','id':2},
		{'name':'Communications','id':3}
	];
}]);