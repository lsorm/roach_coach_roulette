$('button').click(function() {
    if ($(this).hasClass('category') || $(this).hasClass('price') ) {
        if ($(this).hasClass('category')){
            $("#category").attr("value", $(this).text());
        }
        if ($(this).hasClass('price')){
            var selected_price = 0;
            if ($(this).hasClass('one')){
                selected_price = 1;
            }
            if ($(this).hasClass('two')){
                selected_price = 2;
            }
            if ($(this).hasClass('three')){
                selected_price = 3;
            }
            $("#price").attr("value", selected_price);
        }
        $('.box').each(function() {
            if ($(this).offset().left < 0) {
                $(this).css("left", "150%");
            }
            else if ($(this).offset().left > $('#container').width()) {
                $(this).animate({
                    left: '50%',
                }, 500 );
            }
            else {
                $(this).animate({
                    left: '-150%',
                }, 500 );
            }
        });
    }
    else {
        if ($(this).hasClass('distance')){
            $("#distance").attr("value", $(this).children('span').text());
            console.log($(this).children('span').text());
        }
    }
});