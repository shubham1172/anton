window.onload = function() {
  var delete_schema = document.getElementById("delete_schema");
  delete_schema.onclick = function() {
    var schemas = document.getElementsByTagName("input");
    var checked = [];
    for (var i = 0; i < schemas.length; i++) {
        if (schemas[i].checked) {
          checked.push(schemas[i]);
        }
    }
    if(checked.length===0){
      var message=document.getElementById("message");
      message.innerHTML='Select schema(s) to be deleted.'
    }
    else{
      var request = new XMLHttpRequest();
      request.open('POST', '/api/drop-schema', true);
      request.setRequestHeader('Content-Type', 'application/json');
      request.send(JSON.stringify({schema: "testanuja"}));
      window.location.replace('/model');
    }
  }
}
