//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");
var assert = require('assert');
var fs = require('fs');

var chai = require('chai');
var expect = chai.expect;
chai.use(require('chai-json'));
// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

// UNIT test begin
describe('GET /', function() {
      it('respond with html', function(done) {
         server
         .get('/')
         .expect('Content-Type', /html/)
         .expect(200, done);
      });
});

describe('GET /json/:name ', function () {

      it('contain correct value for all operations', function () {
            server
              .get('/json/operations.json')
              .expect('Content-Type', /html/)
              .expect(200)
              .expect((res) => {
                var match = res.text.match(/(?<=<tr>).*?(?=<\/tr>)/gm)
                for (line of match) {
                  var object = line.match(/(?<=<td>).*?(?=<\/td>)/gm)
                  if (object != null) {
                        assert.equal(eval(object[0] + object[1] + object[2]), object[3])
                  }
                }
              });
          });
        });

describe('Check operations.json', function () {
      it('is a json file', function (done) {
        expect('./operations.json').to.be.a.jsonFile();
        done()
      });
    
      it('x = 1, y = 2, op +', function () {
        expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
          "x": 1,
          "y": 2,
          "op": "+"
        })
      });
      it('x = 3, y = 2, op -', function () {
            expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
              "x": 3,
              "y": 2,
              "op": "-"
            })
      });
      it('x = 3, y = 5, op *', function () {
            expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
              "x": 3,
              "y": 5,
              "op": "*"
            })
      });
      it('x = 15, y = 5, op /', function () {
      expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
            "x": 15,
            "y": 5,
            "op": "/"
      })
      });

});