window.onload = function() {
  var delete_table = document.getElementById("delete_schema");
  delete_schema.onclick = function() {
    var tables = document.getElementsByTagName("input");
    var checked = [];
    for (var i = 0; i < tables.length; i++) {
        if (tables[i].checked) {
          checked.push(tables[i]);
        }
    }
    if(checked.length===0){
      var message=document.getElementById("message");
      message.innerHTML='Select table(s) to be deleted.'
    }
    else{
      var request;
      for (var j=0; j<=checked.length; j++){
        request = new XMLHttpRequest();
        request.open('POST', '/api/drop-table', true);
        request.setRequestHeader('Content-Type', 'application/json');
        request.send(JSON.stringify({table: checked[j].value}));
      }
      request.onload = function(){
        if(request.readystate = XMLHttpRequest.DONE){
          //redirect to model
          window.location="http://localhost/model";
        }
      }
    }
  }
}
