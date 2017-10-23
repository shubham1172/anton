window.onload = function(){
  var create_table = document.getElementById('create_table');
  var url=window.location.href;
  var arr=url.split("/");
  var sql_query = document.getElementById('create_table_query');
  sql_query.placeholder="CREATE table "+arr[4]+".<tablename>(col_name col_definition, col_name col_definition);";

  /*var counter=0;

  function createTemplate(counter){
    var id=counter;
    var htmlTemplate=
    `${id}.<tr id=${id}>
        <td>Column name: </td>
        <td><input type="text" name="column_name" placeholder="Enter column name"></td>
        <td><select name="column_type">
          <option value="" disabled selected>Select column type</option>
          <option value="char">Character</option>
          <option value="boolean">Boolean</option>
          <option value="integer">Integer</option>
          <option value="decimal">Decimal</option>
          <option value="varchar">String</<option>
          <option value="date">Date</<option></select>
        </td>
        <td><select id=cc${id} name="column_contraint">
          <option value="" disabled selected>Select column contraint</option>
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

  add_column.onclick = function(){
    counter+=1;
    column = createTemplate(counter);
    var container = document.createElement("div");
    container.innerHTML = column;
    document.getElementById("column_details").appendChild(container);
    document.getElementById("cc"+counter).onchange = function(){constraint_check(this,counter)};
    document.getElementById("table"+counter).onchange = function(){ foreign_key_attribute(this,counter)};
    }

    function constraint_check(that,counter) {
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
*/
  create_table.onclick = function(){
    var request;
    var sql_query = document.getElementById('create_table_query').value;
    request = new XMLHttpRequest();
    request.open('POST', '/api/raw-sql', true);
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.stringify({query: sql_query}));
    request.onload = function(){
      if(request.readystate = XMLHttpRequest.DONE){
        var message = document.getElementById("message");
        var msg = JSON.parse(request.responseText);
        if (msg.message=="no results to fetch"){
          message.innerHTML="Table succesfully created!";
        }
        else{
            message.innerHTML=msg.message;
        }
      }
    }
  }
}
