window.onload = function () {
  var message=document.getElementById("message");

  document.getElementById('import').onclick = function() {
        var formatted_data, data, files;
        files = document.getElementById('table_data').files;
        if (files.length <= 0)
        message.innerHTML='Kindly select a file.';
      else if (files[0].type!="application/json")
        message.innerHTML='Select a JSON file.';
      else {
        var read_data = new FileReader();
        read_data.onload = function(file_data) {
          data = JSON.parse(file_data.target.result);
          console.log(formatted_data);
          var table_name = document.getElementById('table_name').value;
          var url=window.location.href;
          var arr=url.split("/");
          var schema_name = arr[4];
          var request = new XMLHttpRequest();
          request.open('POST', '/api/import-table', true);
          request.setRequestHeader('Content-Type', 'application/json');
          request.send(JSON.stringify({table: table_name,schema: schema_name,data: data}));
          request.onload = function(){
            if(request.responseText.code = 200){
              window.location = "http://localhost/model/"+arr[4];
            }
          }
        }
        read_data.readAsText(files.item(0));
      }
    }
}
