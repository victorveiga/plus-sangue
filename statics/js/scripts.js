function goTo(params) {
    location.href = params
}

$(document).ready(function(){
    var $doc = $('html, body');
    $('section a[href^="#"]').click(function(e){
        e.preventDefault()
        $doc.animate({
            scrollTop: $( $.attr(this, 'href') ).offset().top
        }, 500);
        return false;
        
    });
});

    

