function getHTML(column_name, row, length) {
  var html="<tr>";
  for (var i=0 ; i<length ; i++)
  {
    html+="<td><b>"+column_name[i]+"</b></td>";
  }
  html+="</tr>";
  for (var i=0 ; i<row.length ; i++)
  {
    html+="<tr>";
    for(var j=0 ; j<length ; j++) {
      html+="<td id="+row[i][j]+" ondblclick='addInput(this);'>"+row[i][j]+"</td>";
    }
    html+="</tr>";
  }
  return html;
}

function closeInput(elm) {
    var td = elm.parentNode;
    var value = elm.value;
    td.removeChild(elm);
    //updateTable(value, id);
    td.innerHTML = value;
}

function addInput(elm) {
    if (elm.getElementsByTagName('input').length > 0) return;
    var value = elm.innerHTML;
    elm.innerHTML = '';
    var input = document.createElement('input');
    input.setAttribute('id', elm.id);
    input.setAttribute('type', 'text');
    input.setAttribute('value', value);
    input.setAttribute('onBlur', 'closeInput(this)');
    elm.appendChild(input);
    input.focus();
}

window.onload = function() {

  var url=window.location.href;
  var arr=url.split("/");
  var request = new XMLHttpRequest();
  request.open('POST', '/api/get-table-data', true);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send(JSON.stringify({table: arr[5],schema: arr[4]}));
  request.onload = function(){
    if(request.readystate = XMLHttpRequest.DONE){
      var response = JSON.parse(request.responseText);
      if(response.data.message == "Table doesn't exists or is empty") {
        document.getElementById("message").innerHTML = "Table is empty!";
      }
      else {
        var column_name = response.data.headers;
        var row = response.data.values;
        var length = column_name.length;
        document.getElementById('table_data').innerHTML = getHTML(column_name, row, length);
      }
    }
  }

}
