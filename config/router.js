/**
* Router file, manages the routing for app
*/

var express = require('express');
var router = express.Router();
var path = require('path');

router.get('/', function(req, res){
	res.status(200).send("Homepage");
});

module.exports = router;
