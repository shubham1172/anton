window.onload = function() {
  var rename_table = document.getElementById('rename_table');

  rename_table.onclick = function(){
      var url=window.location.href;
      var arr=url.split("/");
      var request = new XMLHttpRequest();
      var new_name = document.getElementById('table_name').value;
      request.open('POST', '/api/rename-table', true);
      request.setRequestHeader('Content-Type', 'application/json');
      request.send(JSON.stringify({schema: arr[4],table: arr[5],new_name: new_name}));
      request.onload = function(){
        if(request.readystate = XMLHttpRequest.DONE){
          history.go(-1);
        }
    }
  }
}
