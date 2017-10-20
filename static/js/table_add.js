window.onload = function(){
  var create_table = document.getElementById('create_table');
  var add_column = document.getElementById('add_column');

  var column=`<tr>
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
      <td><select name="column_contraint" onchange="foreign_keyk(this);">
        <option value="" disabled selected>Select column contraint</option>
        <option value="NOT NULL">NOT NULL</option>
        <option value="PRIMARY KEY">PRIMARY KEY</option>
        <option value="UNIQUE">UNIQUE</option>
        <option value="FOREIGN KEY">FOREIGN KEY</option>
        <option value="CHECK">CHECK</option></select>
      </td>
      <td>
        <select id="fk" name="tables" style="display: none;" onchange="foreign_key(this);">
        <option value="" disabled selected>Select your option</option>
      </td>
    </tr>`;
    
  add_column.onclick = function(){
    document.getElementById('column_details').innerHTML+=column;
  }

  function foreign_key(that){
    if (that.value == "FOREIGN KEY") {
            document.getElementById("fk").style.display = "block";
        }
  }
}
