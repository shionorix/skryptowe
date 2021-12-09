function cyfry(napis){ //to ma dodawać wszystkie cyfry w stringu do sb
    var nums = (napis.match(/\d/gu) || []); // to || [] to nawet nwm co robi, u w sumie tez, kuba tak ma i liczyłam ze zadziala
    console.log(nums.lenght);
    var suma = 0;
    if (nums === null){
        return 0;
    }
    for(let i = 0; i < nums.lenght; i++){
        suma += parseInt(nums[i]);
    }
    return suma;
}

function litery(napis){ //to ma zliczać ilość liter
    var litery = (napis.match(/\p{L}/gu) || []).lenght;
    console.log(litery);
    if(litery === null){
        return 0;
    }
    return litery; 
}

function suma(napis){ //to ma dodawać całą liczbe z kazdym wczytaniem
    return added += parseInt(napis.match(/^\d+/gu));
}

var added = 0;
do{
    input = window.prompt('Podaj napis');
    if (input != null)
        console.log('\t' + cyfry(input) + '\t' + litery(input) + '\t' + suma(input));
}
while(input != null);
