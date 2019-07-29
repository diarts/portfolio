// #2d204e
var TOGGLE_MAIN_COLOR = 'rgb(45, 32, 78)';
// #4364bd
var TOGGLE_SECOND_COLOR = 'rgb(67, 100, 189)';
var MIN_FONT_SIZE = 12;

$(document).ready(() => {

    $('.nav_list').each(function () {
        $(this).find('.list_toggle').each(function () {

            let child_color = undefined;
            if ($(this).css('background-color') == TOGGLE_MAIN_COLOR) {
                child_color = TOGGLE_SECOND_COLOR;
            } else {
                child_color = TOGGLE_MAIN_COLOR;
            }

            let parent_font_size = parseInt($(this).css('font-size'));
            let children_ul = $(this).children('ul');

            if (children_ul.length !== 0) {
                switch (children_ul.attr('class')) {
                    case 'dropdown':
                        children_ul.css('top', '100%');
                        break;
                    case 'dropleft':
                        children_ul.css({right: '100%', top: '0px'});
                        break;
                    case 'dropright':
                        children_ul.css({left: '100%', top: '0px'});
                        break;
                    case 'dropup':
                        children_ul.css('bottom', '100%');
                        break;
                }

                children_ul.css('background-color', child_color);

                if (parent_font_size > MIN_FONT_SIZE) {
                    children_ul.css('font-size', `${parent_font_size - 2 + 'px'}`)
                }
            }

            $(this).children('.hover_background_down').css('background-color', child_color);
            $(this).children('.hover_background_up').css('background-color', child_color);
        });
    });
});

$('.nav_list').ready(function () {
    $("li").hover(function () {
        if ($(this).children('.nav_hover_line').hasClass('unhovered')) {
            $(this).children('.nav_hover_line').removeClass('unhovered');
        }
        $(this).children('.nav_hover_line').addClass('hovered');
    }, function () {
        $(this).children('.nav_hover_line').addClass('unhovered');
        $(this).children('.nav_hover_line').removeClass('hovered');
    });
});
