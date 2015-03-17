// based on https://github.com/tiagocparra/angularJS-socketIO/blob/master/angular-socket.js
var module = angular.module('socket.io', []);

module.provider('$socket', function $socketProvider() {
	var ioUrl = '';
	var ioConfig = {};

	// set socket.io connection url
	this.setUrl = function setUrl(url){
		if(typeof url == 'string'){
			ioUrl = url;
		}
		else{
			throw new TypeError('Invalid Type. Url must be String.');
		}
	};
	
	this.$get = function $socketFactory($rootScope) {
    	var socket = io(ioUrl, ioConfig);
	    return{
	    	// event listener for socket.on event 
            on : function on(event, callback){
                socket.on(event, function(){
                    var args = arguments;
                    $rootScope.$apply(function () {
                        callback.apply(socket, args);
                    });
                });
            },
            // removing event listeners to prevent memory leaks
            off: function off(event, callback) {
                if (typeof callback == 'function') {
                    socket.removeListener(event, callback);
                } else {
                    socket.removeAllListeners(event);
                }
            },
            // for sending data to the server
            emit: function emit(event, data, callback) {
                if (typeof callback == 'function') {
                    socket.emit(event, data, function () {
                        var args = arguments;
                        $rootScope.$apply(function () {
                            callback.apply(socket, args);
                        });
                    });
                }    
                else{
                    socket.emit(event, data);
                }
            }
	    };
	};
});