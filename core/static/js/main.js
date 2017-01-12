/**
 * Created by sp41mer on 17.12.16.
 */

const resultUrl = '/marks/result/'
var cards;

function show(cards,trigger){

    if (cards.length>0){
        cards.first().show();
        cards.splice(0,1);
    }
    else {
       if (trigger>0) {
            swal({
                title: "Поля заполнены",
                text: "Оценка сохранена",
                type: "success",
                confirmButtonText: "OK",
                closeOnConfirm: false
            },
                function(){
                    var ratedUser = window.location.href.split('/').slice(-1)[0];
                    window.location = resultUrl+ratedUser;
                });
         }
    }
}

$(document).ready(function(){
    cards = $('.scoring-card');
    show(cards,0);
    $('.button-grid__button').click(function(){
        var correct = true;
        var arrayOfMarks = $(this).parent().parent().find('input');
        arrayOfMarks.each(function(key,value){if (value.value == '') correct = false})
        if (correct){
            $(this).parent().parent().hide();
            show(cards,1);
        }
        else{
            swal("Ошибка","Заполните поля","error")
        }

    });
});

$(".js-form-submit").submit(function (e) {
    e.preventDefault();
    var url = $(this).attr('action');
    var user_id = $(".marked_user__id").val();
    var data = $(this).serialize() + "&user_id=" + user_id;

    $.post(url, data)
});

$('.graph').percentcircle();

//КУСОК С ВАЛИДАЦИЕЙ
$('.scoring-card__row__input').keyup(function () {
    if ($(this).val()>10 || $(this).val()<0){
        $(this).val(0);
    }
});




