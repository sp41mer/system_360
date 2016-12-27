/**
 * Created by sp41mer on 17.12.16.
 */

var cards;

function show(cards,trigger){

    if (cards.length>0){
        cards.first().show();
        cards.splice(0,1);
    }
    else {
        if (trigger>0) {
            swal("Поля заполнены", "Оценка сохранена", "success");
        }
    }
}

$(document).ready(function(){
    cards = $('.scoring-card');
    show(cards,0);
    $('.button-grid__button').click(function(){
        $(this).parent().parent().hide();
        show(cards,1);
    });
});

$(".js-form-submit").submit(function (e) {
    e.preventDefault();

    var url = $(this).attr('action');
    var user_id = $(".marked_user__id").val();
    var data = $(this).serialize() + "&user_id=" + user_id;
    // TODO: валидация
    $.post(url, data)
});

$('.graph').percentcircle();
