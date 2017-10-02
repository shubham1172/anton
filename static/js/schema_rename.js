window.onload = function() {
  var rename_schema = document.getElementById('rename_schema');

  rename_schema.onclick = function(){
      var url=window.location.href;
      var arr=url.split("/");
      var request = new XMLHttpRequest();
      var new_name = document.getElementById('schema_name').value;
      request.open('POST', '/api/rename-schema', true);
      request.setRequestHeader('Content-Type', 'application/json');
      request.send(JSON.stringify({schema: arr[4],new_name: new_name}));
      /*request.onload = function(){
        if(request.readystate = XMLHttpRequest.DONE){
          //redirect to model
        }
    }*/
  }
}
