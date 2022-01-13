// No use of any template system
const { table } = require('console');
var express = require('express'),
    fs = require('fs'),
    logger = require('morgan');


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

var app = express();
var x = 1;
var y = 2;

var result = x + y;
// Determining the contents of the middleware stack
app.use(logger('dev'));                         // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', function (req, res) {     // The first route
    res.send(`${x} + ${y} = ${result}`); // Send a response to the browser
});

app.get('/json/:name', function (req, res) {
    var jsonFile = JSON.parse(readFile(req.params.name))

    printedTable = '<table border="2"><tr> <th> x </th> <th> Operation </th> <th> y </th> <th> Result </th> </tr>'

    for (var object of jsonFile) {
        printedTable += `<tr> <td> ${object.x} </td> <td> ${object.op} </td> <td> ${object.y} </td> <td> ${eval('' + object.x + object.op + object.y)} </td> </tr>`
    }
    printedTable += '</table>'

    res.send(printedTable);
});
// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});