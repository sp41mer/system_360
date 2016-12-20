/**
 * Created by sp41mer on 17.12.16.
 */

var cards;

function show(cards){
    if (cards.length>0){
        cards.first().show();
        cards.splice(0,1);
    }
    else swal("Поля заполнены", "Оценка сохранена", "success");
}

$(document).ready(function(){
    cards = $('.scoring-card');
    show(cards);
    $('.button-grid__button').click(function(){
        $(this).parent().parent().hide();
        show(cards);
    });
});