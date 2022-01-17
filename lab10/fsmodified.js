var http = require("http");
var fs = require("fs");

async function pathHandler(response, path) {
    fs.stat(path, (error, stats) => {
        if (error) {
            console.log(error);
            response.write("There is no such file/directory.");
            response.end();
        }
        else {
            if (stats.isFile()){
                fs.readFile(path, (error, data) => {
                    if (error) {
                        response.write("Error occured while reading a file");
                        response.end();
                    }
                    response.write(`${path} is a file.\nContents:\n${data}`);
                    response.end();
                });
                
            }
            else if(stats.isDirectory()) {
                response.write(`${path} is a directory.`);
                response.end(); 
            } 
        }
    });
}


function requestListener(request, response) {
    console.log("--------------------------------------");
    console.log("The relative URL of the current request: " + request.url + "\n");
  
    var url = new URL(request.url, `http://${request.headers.host}`);
  
    if (url.pathname == '/submit') {
      /* ************************************************** */
      response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
      /* ************************************************** */
      if (request.method == 'GET') {
        pathHandler(response, url.searchParams.get('path'));
      }
      else {
        response.write(`This application does not support the ${request.method} method`);
        response.end();
      }
    }
    else {
      response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      /* ************************************************** */
      response.write(`<form method="GET" action="/submit">
                    <label for="path">Podaj ścieżkę</label>
                    <input name="path">
                    <br>
                    <input type="submit">
                    <input type="reset">
                  </form>`);
      /* ************************************************** */
      response.end();
    }
  }
  
  /* ************************************************** */
  /* Main block
  /* ************************************************** */
  var server = http.createServer(requestListener); 
  server.listen(8080);
  console.log("The server was started on port 8080");
  console.log("To stop the server, press 'CTRL + C'");