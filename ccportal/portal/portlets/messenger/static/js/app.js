var app = angular.module('chatApp', [ 'socket.io' ]);

// configuration for the socket app
app.config(function ($socketProvider) {
    $socketProvider.setUrl(':3000/');
});

// controller
app.controller('chatCtrl', function(data){

	// message received
	$socket.on('message', function(data){

	});
	// user typing
	$socket.on('typing', function(data){

	});
	// user disconnects
	$socket.on('disconnect', function(data){

	});
	// send message broadcast
	$scope.emit = function emit(){
		$socket.emit('message', $scope.message);
	};
});