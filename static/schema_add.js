document.onload = function() {
  var create_schema = document.getElementById('create_schema');
  create_schema.onclick = function(){
    console.log('hi');
    var request = new XMLHttpRequest();
    var schema = document.getElementById('schema_name').value;
    request.open('POST', '/api/create-schema', true);
    request.setRequestHeader('Content-Type', 'application/json');
    request.send(JSON.stringify({schema: schema}));
  };
};
