// Application using the 'Pug' template system
var express = require('express'),
    logger = require('morgan'),
    fs = require('fs');
var app = express();
var x = 1;
var y = 2;

function isFile(path) {
    try {
        if (fs.existsSync(path)) {
            if (fs.statSync(path).isFile()){
                return true
            }
            return false
        }
        return false
    }
    catch (err) {
        return false
    }
}

function readFile(path) {
    if (isFile(path)){
        return fs.readFileSync(path, {encoding:"utf-8"});
    }
    else{
        return null
    }
}

result = x + y;
// Configuring the application
app.set('views', __dirname + '/views'); // Files with views can be found in the 'views' directory
app.set('view engine', 'pug');          // Use the 'Pug' template system

// Determining the contents of the middleware stack
app.use(logger('dev'));                         // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', function (req, res) {      // The first route
    res.render('index', { result: `${x} + ${y} = ${result}` }); // Render the 'index' view in 'pretty' mode — the resulting HTML code will be indented — the 'pretty' option has the 'deprecated' status — in the future it will not be supported
    //res.render('index '); // Render the 'index' view; because the 'pretty' mode is, by default, turned off so the resulting HTML will be without indentation
});

app.get('/json/:name', function (req, res) {
    var json = JSON.parse(readFile(req.params.name))

    res.render('json', { json: json });
});

// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});