function exportTable() {
  var textToSave = "anuja";
  var filename = 'file.json';
  var blob = new Blob([textToSave], {type: "text/plain;charset=utf-8"});
  saveAs(blob, filename);
}
/*window.onload = function () {
  var table_export = document.getElementById('export');

  function exportTable(table, data)
  {

  }
  table_export.onclick = function () {
    var textToSave = "anuja";
    var filename = 'file.json';
    var blob = new Blob([textToSave], {type: "text/plain;charset=utf-8"});
    saveAs(blob, filename);
  }
}*/
