$(document).ready(function() {
//     $("p").click(function(){
//         alert("Clicky clicky");
//         $(this).hide();
//     });
    $("p").on({
        mouseenter: function(){
            $(this).css("background-color", "lightgray");
        },
        mouseleave: function(){
            $(this).css("background-color", "blue");    
        },
        click: function(){
            $(this).css("background-color", "#ac7");
        },
    });
});

