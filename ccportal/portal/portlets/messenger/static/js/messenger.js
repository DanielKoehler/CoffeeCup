
var messenger = angular.module('messenger', [
  'bd.sockjs',
  'angucomplete'
]);

messenger.factory('messengerSocket', function (socketFactory) {
  return socketFactory({
    url: 'http://localhost:9999/messenger'
  });
})

messenger.controller('MessengerCtrl', function($scope, $http, messengerSocket) {

  $scope.active_thread = null;
  $scope.threads = {};

  $scope.message = "";
  $scope.max = 140;

  $scope.selectedPerson = null;
  $scope.selectedPersonFeildValue = "";

  $scope.people = [];

  $scope.addMessage = function() { 

    messengerSocket.send(JSON.stringify({'event':'addMessage', 'message':$scope.message, 'thread': $scope.threads[$scope.active_thread].id}));
    $scope.message = "";

  };

  $scope.$watch('selectedPerson', function() {
    if($scope.selectedPerson != null){
      $scope.createThread($scope.selectedPerson.originalObject.id)  
    }
  });

  $scope.createThread = function(id){

      

      for (var t in $scope.threads){

        console.log($scope.threads[t])

        if ($scope.threads[t]['users'][0].id == id){
          $scope.selectThread($scope.threads[t].id)
          return;
        }
      }

      messengerSocket.send(JSON.stringify({'event':'addThread', 'users': [id]}));

      $scope.selectedPerson = null;

  }  

  $scope.selectThread = function(id){

      // messengerSocket.send(JSON.stringify({'event':'addThread', 'message':$scope.message, 'thread': $scope.threads[$scope.active_thread].id}));
      console.log(id)
      $scope.active_thread = id
      $scope.selectedPersonFeildValue = ""; 

  }

  messengerSocket.setHandler('open', function (message){

    console.log("Opened socket");
  
  })

  

  messengerSocket.setHandler('message', function(packet) {

    var obj = packet.data;

    console.log("obj", obj);

    switch(packet.data.route){
      case "thread":
        if ($scope.active_thread == null)
          $scope.active_thread = obj.data.id
        console.log("Received a thread");
        $scope.threads[obj.data.id] = obj.data;
      break;
      case "message":
        $scope.threads[obj.data.thread].messages.push(obj.data);
      break;
    } 
  
  });

  $http.get('/useradministration/users/get/', {}).

    success(function(people, status, headers, config) {
      // this callback will be called asynchronously
      // when the response is available
      if (status == 200){

        $scope.people = people

      }

    }).
    error(function(data, status, headers, config) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
      ngDialog.open({
          template: '<h3>Something awful happened...</h3><p>The message the server sent back was: &ldquo;{{ngDialogData.message}}&rdquo;</p><p>Please contact your system admistrator if this error persists.</p>',
          plain: true,
          data: { message : data.message }
      });
  });

});