angular.module('app.controllers', [])

.controller('pageCtrl', ['$scope', '$stateParams', '$http', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams, $http) {

  $scope.getTemp=function(){
    $http.get('http://192.168.100.54:5000/all').then(function(response){
      $scope.temp1=response.data.temp1;
      $scope.temp2=response.data.temp2;
      $scope.hum=response.data.hum;

    });
  };


}])
