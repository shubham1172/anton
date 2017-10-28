function getHTML(column_name, length) {
  var html="";
  for (var i=0 ; i<length ; i++)
  {
    html+="<tr><td>"+column_name[i].name+":</td><td>"+"<input name=\"row_data\" type=\"text\"></td></tr>";
  }
  return html;
}

window.onload = function() {

  var url=window.location.href;
  var arr=url.split("/");
  var request = new XMLHttpRequest();
  request.open('POST', '/api/get-table-info', true);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send(JSON.stringify({table: arr[5],schema: arr[4]}));
  request.onload = function(){
    if(request.readystate = XMLHttpRequest.DONE){
      var response = JSON.parse(request.responseText);
      var column_name = response.data.columns;
      var length = column_name.length;
        document.getElementById('table_insert').innerHTML = getHTML(column_name, length);
    }
  }

  var insert_data = document.getElementById('insert_data');
  insert_data.onclick = function () {
    var row = document.getElementsByTagName('input').value;
    }

}
