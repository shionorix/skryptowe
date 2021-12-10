function wykonaj() {
    var input = document.forms[0].elements.tekst.value;
    var storage = document.forms[0].elements.webstorage.checked;
    console.log(input, storage);
}

document.forms[0].elements.wykonaj.onclick = wykonaj;