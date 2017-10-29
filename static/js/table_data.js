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
      html+="<td id="+row[i][j]+" class=\""+column_name[j]+"\" ondblclick='addInput(this);'>"+row[i][j]+"</td>";
    }
    html+="</tr>";
  }
  return html;
}

function updateTable(value, id, name) {
  var url=window.location.href;
  var arr=url.split("/");
  var sql_query;
  if(id=="null") {
    sql_query = "UPDATE "+arr[4]+"."+arr[5]+" SET "+name+"='"+value+"' WHERE "+name+"='';";
  }
  else {
    sql_query = "UPDATE "+arr[4]+"."+arr[5]+" SET "+name+"='"+value+"' WHERE "+name+"='"+id+"';";
  }
  console.log(sql_query);
  var request = new XMLHttpRequest();
  request.open('POST', '/api/raw-sql', true);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send(JSON.stringify({query: sql_query}));
  request.onload = function(){
    if(request.readystate = XMLHttpRequest.DONE){
      var message = document.getElementById("message");
      var msg = JSON.parse(request.responseText);
      if (msg.message=="no results to fetch"){
      }
      else{
        message.innerHTML=msg.message;
      }
    }
  }
}

function closeInput(elm) {
  console.log(elm);
    var td = elm.parentNode;
    var value = elm.value;
    var name = elm.name;
    var id = elm.id;
    td.removeChild(elm);
    updateTable(value, id, name);
    td.innerHTML = value;
    console.log(elm);
}

function addInput(elm) {
    if (elm.getElementsByTagName('input').length > 0) return;
    var value = elm.innerHTML;
    elm.innerHTML = '';
    var input = document.createElement('input');
    input.setAttribute('id', elm.id);
    input.setAttribute('type', 'text');
    input.setAttribute('name', elm.className);
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
