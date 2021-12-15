function ustawOnClick() {
    document.styleSheets[0].disabled = false;
}

function usunOnClick(){
    document.styleSheets[0].disabled = true;
}

document.forms[0].ustaw.onclick = ustawOnClick
document.forms[0].usun.onclick = usunOnClick
