var DROP_ANIMATION_LENGTH = 500;

function show_hide_element(element){
    // add reqursiving toggle close function
}

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

        if ($(this)[0] === sender_element || $.inArray(sender_element, child_array) >= 0) {
            let target_ul = $(this).children('ul');
            let target_ul_class = target_ul.attr('class');

            if (!$(this).hasClass('open')) {
                $(this).addClass('open');
            } else {
                $(this).removeClass('open')
            }

            if (target_ul_class == 'dropdown' || target_ul_class == 'dropup') {
                target_ul.animate({height: "toggle"}, DROP_ANIMATION_LENGTH);
            } else {
                target_ul.animate({width: "toggle"}, DROP_ANIMATION_LENGTH);
            }
        }
    })
});
