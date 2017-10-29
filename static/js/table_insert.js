function getHTML(column_name, length) {
  var html="";
  for (var i=0 ; i<length ; i++)
  {
    html+="<tr><td>"+column_name[i].name+":</td><td>("
      +column_name[i].type+")</td><td>"+"<input name=\"row_data\" type=\"text\"></td></tr>";
  }
  return html;
}

function getValue(inputData){
  return inputData.value;
}

window.onload = function() {

  var url=window.location.href;
  var arr=url.split("/");
  var request = new XMLHttpRequest();
  var column_name = null;
  request.open('POST', '/api/get-table-info', true);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send(JSON.stringify({table: arr[5],schema: arr[4]}));
  request.onload = function(){
    if(request.readystate = XMLHttpRequest.DONE){
      var response = JSON.parse(request.responseText);
      column_name = response.data.columns;
      var length = column_name.length;
        document.getElementById('table_insert').innerHTML = getHTML(column_name, length);
    }
  }

  var insert_data = document.getElementById('insert_data');
  insert_data.onclick = function () {
    var row = Array.from(document.getElementsByTagName('input')).map(getValue);
    var sql_query="INSERT INTO "+arr[4]+"."+arr[5]; var col_names = ""; var col_datas = "";
      for(var i=0;i<column_name.length;i++){
          if(row[i]!=''){
            if(column_name[i].type=='character varying'||column_name[i].type=='text'){
              row[i]="'"+row[i]+"'"
            }
            col_names+=column_name[i].name+", ";
            col_datas+=row[i]+", ";
          }
      }
      if(col_names.length==0){
        document.getElementById('message').innerHTML="No data to insert";
      }else{
        col_names = col_names.substr(0, col_names.length-2); //remove extra comma
        col_datas = col_datas.substr(0, col_datas.length-2); //remove extra comma
        sql_query+="("+col_names+") VALUES("+col_datas+");";
        //console.log(sql_query);
        var insert_request = new XMLHttpRequest();
        insert_request.open('POST', '/api/raw-sql', true);
        insert_request.setRequestHeader('Content-Type', 'application/json');
        insert_request.send(JSON.stringify({query: sql_query}));
        insert_request.onload = function(){
          if(insert_request.readystate = XMLHttpRequest.DONE){
            var response = JSON.parse(insert_request.responseText);
            if(insert_request.status===200){
              toClear = document.getElementsByTagName('input');
              for(var j=0;j<Array.from(toClear).length-1;j++){
                toClear[j].value="";
              }
              document.getElementById('message').innerHTML="Data inserted!";
            }else{
              document.getElementById('message').innerHTML=response.message;
            }
          }
        }
      }
    }
}
