window.onload = function(){
  var alter_table = document.getElementById('alter_table');
  var url=window.location.href;
  var arr=url.split("/");
  var sql_query = document.getElementById('alter_table_query');
  sql_query.value="ALTER TABLE "+arr[4]+"."+arr[5]+" ADD column_name datatype;\nALTER TABLE "+arr[4]+"."+arr[5]+" DROP COLUMN column_name;\nALTER TABLE "+arr[4]+"."+arr[5]+" ALTER COLUMN column_name datatype; ";

  alter_table.onclick = function(){
    var request;
    var sql_query = document.getElementById('alter_table_query').value;
    request = new XMLHttpRequest();
    request.open('POST', '/api/raw-sql', true);
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.stringify({query: sql_query}));
    request.onload = function(){
      if(request.readystate = XMLHttpRequest.DONE){
        var message = document.getElementById("message");
        var msg = JSON.parse(request.responseText);
        if (msg.message=="no results to fetch"){
          message.innerHTML="Table succesfully altered!";
        }
        else{
            message.innerHTML=msg.message;
        }
      }
    }
  }
}
