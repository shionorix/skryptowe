function printdata() {
    alert(document.forms['simpleform'].pole_tekstowe.value + ' - ' + typeof(document.forms['simpleform'].pole_tekstowe.value) + '\n' + document.forms['simpleform'].pole_liczbowe.value + ' - ' + typeof(document.forms['simpleform'].pole_liczbowe.value));
}  
document.forms['simpleform'].wypisz.onclick = printdata