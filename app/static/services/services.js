angular.module('complaints')

.service('complaintService',['$http',
	function($http){
		var api = {};

		api.issue ={
			'postIssue':function( _data, success=null, failure=null){
				return genReq($http({headers:{'Content-Type':'application/json'},method:'POST',url:'/issue',data:_data}), success, failure);
			},
			'getIssues':function(_params, success=null, failure=null){
				return genReq($http({method:'GET',url:'/issues',params:_params}), success, failure);
			}
		}

		api.employee = {
			'getEmployees':function( _params, success, failure){
				return genReq($http({method:'GET',url:'/employees',params:_params}), success, failure);
			}
		}

		function genReq(req, success, failure){
			req.then(function(response){
				console.log(response.data)
				if(response.data.status==='success'){
					console.log('success');
					success(response.data.data);
				}if(response.data.status==='failure'){
					console.log('failure');
					failure(response.data);
				}
			});
		}

		return api;
	}
]);