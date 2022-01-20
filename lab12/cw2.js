
function onRequest_8080(request, res) {
    fs.readFile(__dirname + "/index.html")
    .then(contents => {
        res.setHeader("Content-Type", "text/html");
        res.writeHead(200);
        res.end(contents);
    })
    .catch(err => {
        res.writeHead(500);
        res.end(err);
        return;
    });
}
  
  
function onRequest_8081(request, response) {
// response.writeHead(200, { "Content-Type": "text/plain" });
  let d = new Date()
  response.writeHead(200, { "Content-Type": "text/xml" });
  response.writeHead(200, { "Access-Control-Allow-Origin": "*" });
  response.write(`<div>
    <span id='date'> ${d.toLocaleString()} </span>
  </div>`);
response.end();
}
  
/* ************************************************** */
/* Main block
/* ************************************************** */
var http = require('http');
const fs = require('fs').promises;

http.createServer(onRequest_8080).listen(8080);
http.createServer(onRequest_8081).listen(8081);
console.log("The server was started on port 8080 and 8081");
console.log("To stop the server, press 'CTRL + C'");
