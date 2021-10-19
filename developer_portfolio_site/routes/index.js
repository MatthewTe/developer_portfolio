var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  
  res.render('index', { title: 'Express' });
});

/* Articles Homepage */
router.get("/articles", function(req, res, next) {

  res.render('articles', {title: 'Express'});
});

module.exports = router;
