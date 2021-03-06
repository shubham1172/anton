window.onload = function(){
  var create_table = document.getElementById('create_table');
  var tablename = document.getElementById('table_name');
  var url=window.location.href;
  var arr=url.split("/");
  var sql_query = document.getElementById('create_table_query');
  sql_query.value="CREATE table "+arr[4]+".table_name (\n\tcolumn1 datatype,\n\tcolumn2 datatype,\n\tcolumn3 datatype,\n\t....\n);";

  var counter=0;

  function createTemplate(counter){
    var id=counter;
    var htmlTemplate=
    `${id}.<tr id=${id}>
        <td>Column name: </td>
        <td><input type="text" id=cn${id} name="column_name" placeholder="Enter column name"></td>
        <td><select id=dt${id} name="column_type">
          <option value="" disabled selected>Select column type</option>
          <option value="char">Character</option>
          <option value="boolean">Boolean</option>
          <option value="integer">Integer</option>
          <option value="decimal">Decimal</option>
          <option value="varchar">Character Varying</<option>
          <option value="text">Text</<option>
          <option value="date">Date</<option></select>
        </td>
        <td><select id=cc${id} name="column_contraint">
          <option value="" disabled selected>Select column constraint</option>
          <option value="NOT NULL">NOT NULL</option>
          <option value="PRIMARY KEY">PRIMARY KEY</option>
          <option value="UNIQUE">UNIQUE</option>
          <option value="FOREIGN KEY">FOREIGN KEY</option>
          <option value="CHECK">CHECK</option></select>
        </td>
        <td><input id=check${id} type = text name="check_condition" placeholder="Enter CHECK condition" style="display: none;">
          </input>
        </td>
        <td><select id=table${id} name="tables" style="display: none;">
          <option value="" disabled selected>Select table</option></select>
        </td>
        <td><select id=attribute${id} name="attribute" style="display: none;">
          <option value="" disabled selected>Select attribute</option></select>
        </td>
      </tr>`;
      return htmlTemplate;
}
  var tables;
  var attributes;
  var request;
  var url=window.location.href;
  var arr=url.split("/");
  request = new XMLHttpRequest();
  request.open('POST', '/api/get-tables', true);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send(JSON.stringify({schema: arr[4]}));
  request.onload = function(){
    if(request.readystate = XMLHttpRequest.DONE){
      tables = JSON.parse(request.responseText).data;
    }
  }

  tablename.oninput = function() {
    modify_query(tablename.value, counter);
  }

  function modify_query(tn, counter) {
      sql_query.value="CREATE table "+arr[4]+"."+tn+"( ";
      for (var i=1;i<=counter;i++) {
        sql_query.value+=("\n\t"+document.getElementById("cn"+i).value);
        sql_query.value+=(" "+document.getElementById("dt"+i).value);
        if(document.getElementById('cc'+i).value=="FOREIGN KEY"){
          sql_query.value+=(" REFERENCES "+arr[4]+"."+document.getElementById("table"+i).value);
          sql_query.value+=(" ("+document.getElementById("attribute"+i).value+")");
        }
        else if(document.getElementById('cc'+i).value=="CHECK"){
           sql_query.value+=(" "+document.getElementById("cc"+i).value);
           sql_query.value+=(" ("+document.getElementById("check"+i).value+")");
        }
        else {
          sql_query.value+=(" "+document.getElementById("cc"+i).value);
        }
        sql_query.value+=",";
      }
      sql_query.value =(sql_query.value.slice(0,-1));
      sql_query.value +="\n);";
    }

  add_column.onclick = function(){
    counter+=1;
    column = createTemplate(counter);
    var container = document.createElement("div");
    container.innerHTML = column;
    document.getElementById("column_details").appendChild(container);
    document.getElementById("table"+counter).oninput = function(){ foreign_key_attribute(this,counter)};
    document.getElementById("cn"+counter).oninput = function(){ modify_query(tablename.value,counter)};
    document.getElementById("dt"+counter).oninput = function(){ modify_query(tablename.value,counter)};
    document.getElementById("cc"+counter).oninput = function(){
      constraint_check(this,counter);
      modify_query(tablename.value,counter);}
    document.getElementById("check"+counter).oninput = function(){ modify_query(tablename.value,counter)};
    document.getElementById("table"+counter).oninput = function(){
      foreign_key_attribute(this,counter);
      modify_query(tablename.value,counter);}
    document.getElementById("attribute"+counter).oninput = function(){ modify_query(tablename.value,counter)};
    }



    function constraint_check(that,counter) {
      document.getElementById("check"+counter).style.display = "none";
      document.getElementById("table"+counter).style.display = "none";
      document.getElementById("attribute"+counter).style.display = "none";
      if (that.value == "FOREIGN KEY") {
        var table_option = document.getElementById("table"+counter);
        table_option.style.display = "block";
        for(var i=0; i<tables.length; i++) {
          var opt = document.createElement('option');
          opt.innerHTML = tables[i];
          opt.value = tables[i];
          opt.id = tables[i]+counter;
          table_option.appendChild(opt);
        }
      }
     else if (that.value == "CHECK") {
       var check_option = document.getElementById("check"+counter);
       check_option.style.display = "block";
     }
    }

    function foreign_key_attribute(that,counter) {
      var table_name = that.value;
      var attribute_option = document.getElementById("attribute"+counter);
      attribute_option.style.display = "block";
      var request_att;
      var url=window.location.href;
      var arr=url.split("/");
      request_att = new XMLHttpRequest();
      request_att.open('POST', '/api/get-table-data', true);
      request_att.setRequestHeader('Content-Type', 'application/json');
      request_att.send(JSON.stringify({table: table_name,schema: arr[4]}));
      request_att.onload = function(){
        if(request_att.readystate = XMLHttpRequest.DONE){
          attributes = JSON.parse(request_att.responseText).data.headers;
        }
        for(var i=0; i<attributes.length; i++) {
          var opt_att = document.createElement('option');
          opt_att.innerHTML = attributes[i];
          opt_att.value = attributes[i];
          opt_att.id = attributes[i]+counter;
          attribute_option.appendChild(opt_att);
        }
      }
    }

  create_table.onclick = function(){
    var request;
    var sqlquery = document.getElementById('create_table_query').value;
    if(sqlquery == "CREATE table "+arr[4]+`.table_name (
                  	column1 datatype,
                  	column2 datatype,
                  	column3 datatype,
                  	....
                  );`) {
                        var message = document.getElementById("message");
                        message.innerHTML = "Enter SQL query";
                      }
    else{
      request = new XMLHttpRequest();
      request.open('POST', '/api/raw-sql', true);
      request.setRequestHeader('Content-Type', 'application/json');
      request.send(JSON.stringify({query: sqlquery}));
      request.onload = function(){
        if(request.readystate = XMLHttpRequest.DONE){
          var message = document.getElementById("message");
          var msg = JSON.parse(request.responseText);
          if (msg.data=="executed"){
            message.innerHTML="Table succesfully created!";
          }
          else{
              message.innerHTML=msg.message;
          }
        }
      }
    }
  }
}
