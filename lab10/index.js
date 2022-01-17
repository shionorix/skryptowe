var module = require('./module.js');

var op = new module.Operation(parseInt(process.argv[2]), parseInt(process.argv[3])); 
console.log(op.sum());