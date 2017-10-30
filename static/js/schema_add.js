window.onload = function() {
  var create_schema = document.getElementById('create_schema');
  create_schema.onclick = function(){
    var request = new XMLHttpRequest();
    var schema = document.getElementById('schema_name').value;
    request.open('POST', '/api/create-schema', true);
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.stringify({schema: schema}));
    var message = document.getElementById('message');
    request.onload = function(){
      if(request.readystate = XMLHttpRequest.DONE){
        document.getElementById('schema_name').value="";
        var msg = JSON.parse(request.responseText);
        if(msg.code==200)
              message.innerHTML=msg.data;
        else
             message.innerHTML=msg.message;
      }
    }
  }
}
