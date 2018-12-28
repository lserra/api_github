/* 
Author : Hujjat Nazari
Site : template.pplanet.com
*/

$(document).ready(function() {

    'use strict';

        // Scroll View Demo
    $(".header").on("click",".demo", function (event) {
        event.preventDefault();
        var id  = $(this).attr('href'),
            top = $(id).offset().top;
        $('body,html').animate({scrollTop: top}, 1500);
    });


    // SVG Astronaut
    if (document.getElementById('astronaut-error')) {
        var svg = Snap("#astronaut-error");
        Snap.load("img/astronaut.svg", function(f) {
            var g = f.select("g");
            g.attr({
                transform: 't0,0 s1'
            });
            svg.append(g);
        });
    }
});
