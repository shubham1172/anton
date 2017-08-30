/**
* Server file
*/

//include modules
var express = require('express');
var morgan = require('morgan');
var router = require('./router.js');
var config = require('./config.js')

//app init
var app = express();
app.use(morgan('combined'));
app.use('/', router);

app.listen(config.PORT, function(){
	console.log('Anton started on port:80');
});
