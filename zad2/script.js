'use strict';
function cyfry(napis){ 
    if (napis === null){
        return 0;
    }    
    var nums = napis.match(/\d/g); 
    var suma = 0;
    if (nums === null){
        return 0;
    }    
    for(let i = 0; i < nums.length; i++){
        suma += parseInt(nums[i]);
    }
    return suma;
}

function litery(napis){ 
    if(napis === null){
        return 0;
    }    
    var litery = napis.match(/[a-z]/gi);
    if(litery === null){
        return 0;
    }
    return litery.length; 
}

function suma(napis){ 
    if (napis === null) 
        return added;
    if (napis.match(/^\d+/g))
        added += parseInt(napis.match(/^\d+/g));
    return added;
    }

//Kod wywołania
var added = 0;
do{
    var input = window.prompt('Podaj napis');
    if (input != null)
        console.log(`\t ${cyfry(input)} \t ${litery(input)} \t ${suma(input)}`);
}
while(input != null);

//Testy

var expect = chai.expect;

describe("Funkcja cyfry()", function () {
    it("Zwraca 6 dla 123", function () {
        expect(cyfry("123")).to.equal(6);
    });
    it("Zwraca 6 dla qwerty123", function () {
        expect(cyfry("qwerty123")).to.equal(6);
    });
    it("Zwraca 0 dla qwerty", function () {
        expect(cyfry("qwerty")).to.equal(0);
    });
    it("Zwraca 6 dla qwerty", function () {
        expect(cyfry("123qwerty")).to.equal(6);
    });
    it("Zwraca 0 dla pustego napisu", function () {
        expect(cyfry(null)).to.equal(0);
    });
  });
  
describe("Funkcja litery()", function () {
    it("Zwraca 0 dla 111", function () {
        expect(litery("111")).to.equal(0);
    });
    it("Zwraca 6 dla qwerty123", function () {
        expect(litery("qwerty123")).to.equal(6);
    });
    it("Zwraca 6 dla qwerty", function () {
        expect(litery("qwerty")).to.equal(6);
    });
    it("Zwraca 6 dla 123qwerty", function () {
        expect(litery("123qwerty")).to.equal(6);
    });
    it("Zwraca 0 dla pustego napisu", function () {
        expect(cyfry(null)).to.equal(0);
    });
  });
  
describe("Funkcja suma()", function () {
    beforeEach(function () {
        added = 0;
    });
    it("Zwraca 123 dla 123", function () {
        suma("123");
        expect(added).to.equal(123);
    });
    it("Zwraca 123 dla 123 a po nim a123", function () {
        suma("123");
        suma("a123");
        expect(added).to.equal(123);
    });
    it("Zwraca 246 dla 123 a po nim 123a", function () {
        suma("123");
        suma("123a");
        expect(added).to.equal(246);
    });
    it("Zwraca 0 dla pustego napisu", function () {
        suma(null);
        expect(added).to.equal(0);
    });
  });