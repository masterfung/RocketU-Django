
function toggleRotate() {
    $("#joker").toggleClass("rotate");
    $("#joker-right").toggleClass("rotate");
}

setInterval(toggleRotate, 500);