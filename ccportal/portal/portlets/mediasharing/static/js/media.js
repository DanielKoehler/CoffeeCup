
var mediasharing = angular.module('mediasharing', [
'ngDialog',
'ngCookies',
'ngFileUpload'
]);

mediasharing.run( function run( $http, $cookies ){

    // For CSRF token compatibility with Django
    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
})

mediasharing.directive('ngEnter', function () {

    return function (scope, element, attrs) {

        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {

                scope.$apply(function (){
                    scope.$eval(attrs.ngEnter);
                });

                event.preventDefault();
            }
        });
    };

});

mediasharing.factory('hashFactory', function() {
    return {
        getRandom: function() {
            return Math.round((Math.pow(36, length + 1) - Math.random() * Math.pow(36, length))).toString(36).slice(1);
        }
    };
});

mediasharing.controller('MediaSharingCtrl', function($scope, $http, ngDialog, hashFactory, Upload) {

  $scope.workingPath = "";  

  $scope.directory = {};
  $scope.directory.parent = null;
  $scope.directory.files = [];

  $scope.checkObjectModel = [];
  $scope.selectedAll = false;

  $scope.uploadLimit = 20000;
  $scope.predicate = '-modified';
  $scope.editing = null;
  $scope.preEditPersister = null;

  $scope.addFile = function() { 


    ngDialog.open({
        template: 'uploadForm',
    });

  };  

  $scope.navigate = function(objectId) {

    $http.get('directory/get/' + objectId, {}).

      success(function(data, status, headers, config) {
        // this callback will be called asynchronously
        // when the response is available
        if (status == 200){

          $scope.directory = data

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
  }

  $scope.modify = function(id){
    $scope.preEditPersister = 
    $scope.editing = id;
  };

  $scope.checkAll = function () {



      if ($scope.selectedAll) {
          $scope.selectedAll = false;
      } else {
          $scope.selectedAll = true;
      }

      angular.forEach($scope.directory.files, function (item) {
          $scope.checkObjectModel[item.id] = $scope.selectedAll;
      });
    
      console.log($scope.checkObjectModel);

  };

  $scope.deleteSelected = function(){

    var selectedObjs = [];

    angular.forEach($scope.directory.files, function (item) {
      if($scope.checkObjectModel[item.id]){
        selectedObjs.push(item.id)
      }
    });

    console.log(selectedObjs)
  

    $http.post('objects/delete/', { 
      objects: selectedObjs
    }).success(function(items, status, headers, config) {
        // this callback will be called asynchronously
        // when the response is available
        if (status == 200){
          console.log("Remmoved: ", items)
           
          $scope.trash(items)

        }   

      }).error(function(data, status, headers, config) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
        ngDialog.open({
            template: '<h3>Something awful happened...</h3><p>The message the server sent back was: &ldquo;{{ngDialogData.message}}&rdquo;</p><p>Please contact your system admistrator if this error persists.</p>',
            plain: true,
            data: { message : data.message }
        });

    });


  }

  $scope.updateObject = function(object){
    
    console.log("Update Model")

    var url =  'directory/post/'

    if (!object.isDirectory){
      url = 'file/post/'
    }

    $http.post(url + object.id, { 
      name: object.name
    }).success(function(data, status, headers, config) {
        // this callback will be called asynchronously
        // when the response is available
        if (status == 200){
          console.log("Updated File")
        }

      }).error(function(data, status, headers, config) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
        ngDialog.open({
            template: '<h3>Something awful happened...</h3><p>The message the server sent back was: &ldquo;{{ngDialogData.message}}&rdquo;</p><p>Please contact your system admistrator if this error persists.</p>',
            plain: true,
            data: { message : data.message }
        });

    }); 

      $scope.editing = null;
  };

  $scope.addDirectory = function() { 
    
    var timestamp = new Date().getTime();
  
    $http.post('directory/post/', { 
      name: $scope.conflictSafeFileName('New Directory',  $scope.directory), 
      parent: $scope.workingPath
    }).
      success(function(data, status, headers, config) {
        // this callback will be called asynchronously
        // when the response is available
        if (status == 200){
          $scope.directory.files.push(data)
          $scope.modify(data.id)
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

  };

  $scope.conflictSafeFileName = function(name, directory){

    for (var idx in directory.files){

      file = directory.files[idx] 

      if(file.name == name){
        if (/^([A-Za-z0-9.-\s]+)-([0-9]+)$/.test(name)){
          var parts = name.split('-'); 
          parts[parts.length - 1] = parseInt(parts[parts.length - 1]) + 1;
          name = parts.join('-')
          return $scope.conflictSafeFileName(name, directory)
        } 
        return $scope.conflictSafeFileName(name + "-1", directory)
      }
    }

    return name

  }

  $scope.trash = function (ids) {
     for (var idx in $scope.directory.files){

      if(ids.indexOf($scope.directory.files[idx].id) > -1){
        $scope.directory.files.splice(idx, 1);
      }
    }
  }

  $scope.$watch('files', function () {
      console.log($scope.files);
      $scope.upload($scope.files);
  });

  $scope.upload = function (files) {
      if (files && files.length) {

        

          for (var i = 0; i < files.length; i++) {
              var file = files[i];              
              Upload.upload({
                  url: 'objects/post/',
                  fields:{'name':file.name,'parent':$scope.directory.parent, 'type': file.type, 'size': file.size},
                  file: file
              }).progress(function (evt) {
                  
                  var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                  console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);

              }).success(function (data, status, headers, config) {
                  // console.log('file ' + config.file.name + 'uploaded. Response: ' + data);

                  $scope.directory.files.push(data);


              });
          }
      }
  };

  $scope.navigate('');

});