const fs = require('fs');


function isFile(path) {
    if (fs.existsSync(path) && fs.statSync(path).isFile()){
        return true;
    }
    return false;
}

function isDirectory(path) {
    if (fs.existsSync(path) && fs.statSync(path).isDirectory()){
        return true;
    }
    return false;
}

function readFile(path) {
    if (isFile(path)){
        return fs.readFileSync(path, {encoding:"utf-8"});
    }
}

console.log("is a file: ", isFile(process.argv[2]));
console.log("is a directory: ", isDirectory(process.argv[2]));
console.log("contents: ", readFile(process.argv[2]));

module.exports = {
    isFile,
    isDirectory,
    readFile
}
