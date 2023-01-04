//Nav
var count = 0;
$("#nav_icon").click(function(){
    if (count == 0){
        $(this).html('<i class="fa fa-times"></i>');
        $(this).prop("href", "#left_nav");
        count ++;
    } else {
        $(this).prop("href", "#");
        $(this).html('<i class="fa fa-bars"></i>');
        count = 0;
    }
});


//Tab transition
function openTab(evt, cityName) {
    let i, x, tablinks;
    x = document.getElementsByClassName("tabs");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tab_button");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" primary", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " primary";
}