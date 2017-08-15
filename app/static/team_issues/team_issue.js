angular.module("complaints")

.controller("teamIssueCtrl",["$scope","complaintService",function($scope,complaintService){
	// $scope.issues =[ {'id':'1'},{'id':'2'}]
	complaintService.issue.getIssues(null, 
		function(results){
			$scope.issues = results;
			console.log(results);
		}, null);
}]);