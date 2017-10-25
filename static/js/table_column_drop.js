window.onload = function() {
  var delete_column = document.getElementById('delete_column');

  delete_column.onclick = function(){
      var column_name = document.getElementById('delete_column').name;
      var url=window.location.href;
      var arr=url.split("/");
      var sql_query = "ALTER TABLE "+arr[4]+"."+arr[5]+" DROP COLUMN "+column_name+";";

      var request = new XMLHttpRequest();
      request.open('POST', '/api/raw-sql', true);
      request.setRequestHeader('Content-Type', 'application/json');
      request.send(JSON.stringify({query: sql_query}));
      request.onload = function(){
        if(request.readystate = XMLHttpRequest.DONE){
          var message = document.getElementById("message");
          var msg = JSON.parse(request.responseText);
          if (msg.message=="no results to fetch"){
            location.href = document.referrer;
          }
          else{
            message.innerHTML=msg.message;
          }
        }
    }
  }
}
