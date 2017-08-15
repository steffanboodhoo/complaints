angular.module('complaints')

.controller('formCtrl',['$scope','complaintService',function($scope, complaintService){
	$scope.teams = [
		{'name':'Software Dev','id':1},
		{'name':'Products','id':2},
		{'name':'Communications','id':3}
	];

	var date = new Date();
	date = date.toISOString().split('T')[0];
	$scope.issue = {'creator_id':1, 'description':null, 'date_created':date};

	$scope.submit = function(){
		console.log($scope.issue);
		complaintService.issue.postIssue(
			$scope.issue,
			function(response){
				$scope.description="";
				$scope.team_id=null;
			},
			null
		)
	}
}]);