document.getElementById('cardfill').style.display = "none";
document.getElementById('chooseview').style.display = "none";
document.getElementById('chooseview2').style.display = "none";
let g_chosenstat = "";

function togglechoosecard() {
    var state = document.getElementById('cardselectorholder').style.display;
    console.log("togglestate", state);
    if(state === "none" || state === ""){
        document.getElementById('cardselectorholder').style.display = "flex";
        document.getElementById('plcardfill').style.display = "none";
        document.getElementById('cardfill').style.display = "none";
        document.getElementById('chooseview').style.display = "none";
        document.getElementById('chooseview2').style.display = "none";
    }else{
        document.getElementById('cardselectorholder').style.display = "none";
        document.getElementById('plcardfill').style.display = "flex";
        document.getElementById('chooseview').style.display = "block";
        document.getElementById('chooseview2').style.display = "block";
    }
}

function togglecardview() {
    var state = document.getElementById('plcardfill').style.display;
    if(state === "none" || state === ""){
        document.getElementById('plcardfill').style.display = "flex";
        document.getElementById('cardfill').style.display = "none";
        document.getElementById('chooseview2').innerHTML = g_chosenstat + ": Player's View";
    }else{
        document.getElementById('plcardfill').style.display = "none";
        document.getElementById('cardfill').style.display = "flex";
        document.getElementById('chooseview2').innerHTML = g_chosenstat + ": Psychic's View";
    }

}

//----------------------- Section Name ------------------------------
var form = document.forms["cardselector"];
form.addEventListener('submit',cardselector,false);
function cardselector(e) {
    e.preventDefault();
    var target = e.target || e.srcElement;
    chosenstat = target.elements['chosenability'].value
    g_chosenstat = chosenstat.toUpperCase();
    fetch(`/chosenability/${chosenstat}`)
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        togglechoosecard();

        var modes_db = text;
        document.getElementById('chooseview2').innerHTML = g_chosenstat + ": Player's View";
        for (const [key, value] of Object.entries(modes_db)) {
            document.getElementById('gtit' + key).innerHTML = value['gtit'];
            document.getElementById('gmatch' + key).innerHTML = value['gmatch'];
            document.getElementById('gbody' + key).innerHTML = value['gbody'];
        }
        for (const [key, value] of Object.entries(modes_db)) {
            document.getElementById('plgtit' + key).innerHTML = value['gtit'];
            document.getElementById('plgmatch' + key).innerHTML = value['gmatch'];
        }
    });
}
//------------------------------Above Section Ends ------------------------------

//----------------------- Section Name ------------------------------

//------------------------------Above Section Ends ------------------------------



