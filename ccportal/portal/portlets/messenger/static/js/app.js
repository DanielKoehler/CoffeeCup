
var messenger = angular.module('messenger', [
  'bd.sockjs',
]);

messenger.factory('messengerSocket', function (socketFactory) {
  return socketFactory({
    url: 'http://localhost:9999/messenger'
  });
})

messenger.controller('MessengerCtrl', function($scope, messengerSocket) {

  $scope.active_thread = null;
  $scope.threads = {};

  $scope.message = "";
  $scope.max = 140;

  $scope.addMessage = function() { 

    messengerSocket.send(JSON.stringify({'message':$scope.message, 'thread': $scope.threads[$scope.active_thread].id}));
    $scope.message = "";

  };

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

});