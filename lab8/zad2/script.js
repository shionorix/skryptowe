'use strict';
var expect = chai.expect;
function cyfry(napis) {
  //to ma dodawać wszystkie cyfry w stringu do sb
  var nums = napis.match(/\d/g); // to || [] to nawet nwm co robi, u w sumie
  //to || zwroci pusta tablice jezeli lewa strona jest fałszywa, ale to jest takie robienie kurwy z logiki ze taki kod bedzie szybko nie do zrozumienia
  //https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR
  //https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator
  var suma = 0;
  if (nums === null) {
    return 0;
  }
  for (let i = 0; i < nums.length; i++) {
    suma += parseInt(nums[i]);
  }
  return suma;
}

function litery(napis) {
  //to ma zliczać ilość liter
  //i zlicza <3
  var litery = napis.match(/[a-z]/gi);
  if (litery === null) {
    return 0;
  }
  return litery.length;
}

function suma(napis) {
  //to ma dodawać całą liczbe z kazdym wczytaniem
  //poprawka kochanie - to ma zlicząć sume wszystkich cyfr od załadowania strony. Dodawać kolejne wartości możemy tylko jeżeli obecny ciąg zaczyna się od cyferki
  if (napis.match(/^\d/)) added += cyfry(napis);
  return added;
}

var added = 0;
do {
  input = window.prompt("Podaj napis");
  if (input != null)
    console.log(`
    \t ${cyfry(input)} \t ${litery(input)} \t ${suma(input)}
    `); // te ` ... ` to template literale - podobne do f-stringów z pythona, bardzo przydatne kochanie, popatrz sobie
  //https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
} while (input != null);

describe("Funkcja cyfry()", function () {
  it("Zwraca 3 dla 111", function () {
    expect(cyfry("111")).to.equal(3);
  });
  it("Zwraca 3 dla a$%^!dsW1@1_1aaa_", function () {
    expect(cyfry("a$%^!dsW1@1_1aaa_")).to.equal(3);
  });
  it("Zwraca 0 dla asdasd", function () {
    expect(cyfry("asdasd")).to.equal(0);
  });
});

describe("Funkcja litery()", function () {
  it("Zwraca 0 dla 111", function () {
    expect(litery("111")).to.equal(0);
  });
  it("Zwraca 7 dla a$%^!dsW1@1_1aaa_", function () {
    expect(litery("a$%^!dsW1@1_1aaa_")).to.equal(7);
  });
  it("Zwraca 6 dla asdasd", function () {
    expect(litery("asdasd")).to.equal(6);
  });
});

describe("Funkcja litery()", function () {
  it("Zwraca 0 dla 111", function () {
    expect(litery("111")).to.equal(0);
  });
  it("Zwraca 7 dla a$%^!dsW1@1_1aaa_", function () {
    expect(litery("a$%^!dsW1@1_1aaa_")).to.equal(7);
  });
  it("Zwraca 6 dla asdasd", function () {
    expect(litery("asdasd")).to.equal(6);
  });
});

describe("hooks", function () {
  before(function () {
    var added = 0;
  });
  beforeEach(function () {
    added = 0;
  });
  afterEach(function () {
    added = 0;
  });

  it("Zwraca 6 dla 123", function () {
    suma("123");
    expect(added).to.equal(6);
  });
  it("Zwraca 6 dla 123 a po nim a123", function () {
    suma("123");
    suma("a123");
    expect(added).to.equal(6);
  });
  it("Zwraca 12 dla 123 a po nim 123a", function () {
    suma("123");
    suma("123a");
    expect(added).to.equal(12);
  });
});