function import_table(data) {
  var table_name = document.getElementById('table_name').value;
  console.log(table_name);
  var url=window.location.href;
  var arr=url.split("/");
  var schema_name = arr[4];
  console.log(schema_name);
  var request = new XMLHttpRequest();
  request.open('POST', '/api/import-table', true);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send(JSON.stringify({table: table_name,schema: schema_name,data: data}));
  request.onload = function(){
    if(request.readystate = XMLHttpRequest.DONE){
      console.log('done');
    }
  }
}

window.onload = function () {
  var files = document.getElementById('table_data').files;
  var message=document.getElementById("message");

  document.getElementById('import').onclick = function() {
      var formatted_data;
      if (files.length <= 0)
        message.innerHTML='Kindly select a file.';
      else if (files[0].type!="application/json")
        message.innerHTML='Select a JSON file.';
      else {
        var read_data = new FileReader();
        read_data.onload = function(file_data) {
        var data = JSON.parse(file_data.target.result);
        formatted_data = JSON.stringify(data, null, 2);
        console.log(formatted_data);
        }
        read_data.readAsText(files.item(0));
        import_table(formatted_data);
      }
    }

}
