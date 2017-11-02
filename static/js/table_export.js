function exportToFile(data,table) {
  var textToSave = data;
  var filename = table;
  var blob = new Blob([textToSave], {type: "text/json"});
  saveAs(blob, filename);
}

function exportTable(that) {
  var table_name = that.id;
  var url=window.location.href;
  var arr=url.split("/");
  var schema_name = arr[4];
  var request = new XMLHttpRequest();
  request.open('POST', '/api/export-table', true);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send(JSON.stringify({table: table_name,schema: schema_name}));
  request.onload = function(){
    if(request.readystate = XMLHttpRequest.DONE){
      exportToFile(request.responseText,table_name);
    }
  }
}
