val = 0;

function loopFuntion() {
    val = document.forms[0].number.value;
    if (val > 0) {
        val--;
        document.forms[0].number.value = val;
        for (let i = 0; i < 10; i++) {
            document.getElementsByTagName('span')[i].childNodes[0].nodeValue = val;
        }
    }
}

setInterval(loopFuntion, 500);
