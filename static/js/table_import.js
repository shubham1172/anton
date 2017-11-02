window.onload = function () {
  var message=document.getElementById("message");

  document.getElementById('import').onclick = function() {
        var formatted_data, data, files;
        files = document.getElementById('table_data').files;
        var read_data = new FileReader();
        read_data.onload = function(file_data) {
          data = JSON.parse(file_data.target.result);
          formatted_data = JSON.stringify(data, null, 2);
          console.log(formatted_data);
          var table_name = document.getElementById('table_name').value;
          var url=window.location.href;
          var arr=url.split("/");
          var schema_name = arr[4];
          var request = new XMLHttpRequest();
          request.open('POST', '/api/import-table', true);
          request.setRequestHeader('Content-Type', 'application/json');
          request.send(JSON.stringify({table: table_name,schema: schema_name,data: formatted_data}));
          request.onload = function(){
            if(request.readystate = XMLHttpRequest.DONE){
              console.log('done');
            }
          }
        }
        read_data.readAsText(files.item(0));
}
}
