var DROP_ANIMATION_LENGTH = 500;

$(document).ready(() => {

    $('.list_toggle').hover(function () {
        let arrow = $(this).children('.open_arrow');
        let background_down = $(this).children('.hover_background_down');
        let background_up = $(this).children('.hover_background_up');

        if (!$(this).hasClass('open')) {
            if (!arrow.hasClass('hover')) {
                arrow.addClass('hover');
                background_down.addClass('hover');
                background_up.addClass('hover');
            } else {
                arrow.removeClass('hover');
                background_down.removeClass('hover');
                background_up.removeClass('hover');
            }
        }
    }).click(function (e) {
        let sender_element = e.target;
        let child_array = $(this).children();
        child_array = child_array.slice(0, child_array.length - 1);

        if ($(this)[0] === sender_element || $.inArray(sender_element, child_array)>=0) {
            let target_ul = $(this).children('ul');
            let target_ul_class = target_ul.attr('class');

            if (!$(this).hasClass('open')) {
                $(this).addClass('open');
                console.log(DROP_ANIMATION_LENGTH);
                switch(target_ul_class){
                    case 'dropdown':
                        // target_ul.slideDown(500);
                        target_ul.show("slide", {direction: "up"}, DROP_ANIMATION_LENGTH);
                        break;
                    case 'dropup':
                        target_ul.show("blind", {direction: "down"}, DROP_ANIMATION_LENGTH);
                        break;
                    case 'dropleft':
                        target_ul.show("slide", {direction: "right"}, DROP_ANIMATION_LENGTH);
                        break;
                    case 'dropright':
                        target_ul.show("slide", {direction: "left"}, DROP_ANIMATION_LENGTH);
                        break;
                }
            } else {
                $(this).removeClass('open');
                $(this).children('ul').hide(500);
            }
        }
    })
});
