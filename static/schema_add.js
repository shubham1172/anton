window.onload = function() {
  var create_schema = document.getElementById('create_schema');
  create_schema.onclick = function(){
    var request = new XMLHttpRequest();
    var schema = document.getElementById('schema_name').value;
    request.open('POST', '/api/create-schema', true);
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.stringify({schema: schema}));
    var message = document.getElementById('message');
    if(request.readystate = XMLHttpRequest.DONE){
      console.log(JSON.stringify(request.responseText));
      console.log(JSON.stringify(request.responseCode));}
    //console.log(msg);
    message.innerHTML='message';
  }
}
