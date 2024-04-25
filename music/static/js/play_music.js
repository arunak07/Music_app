var i = 0;
var audio = null;

function play(id){
    console.log(id)
    if (i == 0){
        window.audio = document.getElementById(id);   
        audio.play()
        window.i += 1
    }
    if(i == 1){
        audio.pause()
        window.i = 1
        audio1 = document.getElementById(id);
        window.audio = audio1
        audio.play()
    }
}
function pause(id){
    window.i = 0
    audio = document.getElementById(id);
    audio.pause()
}