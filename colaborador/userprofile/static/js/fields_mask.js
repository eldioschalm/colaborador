/**
 * Created by Eldio Schalm on 23/04/2015.
 */

//jQuery(function($){
$(document).ready(function() {
    $('#id_userprofile-0-telefone').mask("(99) 9999-9999");
    $('#id_userprofile-0-cpf').mask('999.999.999-99');

    $("#id_id_userprofile-0-telefone").on("blur", function() {
        var last = $(this).val().substr( $(this).val().indexOf("-") + 1 );

        if( last.length == 3 ) {
            var move = $(this).val().substr( $(this).val().indexOf("-") - 1, 1 );
            var lastfour = move + last;
            var first = $(this).val().substr( 0, 9 );

            $(this).val( first + '-' + lastfour );
        }
    });
});

//$(document).ready(function() {
//    //$("#id_myuserprofile-0-telefone").click(function () {
//    //    alert('campo clicado');
//    //});
//
//});

//if (typeof jQuery != 'undefined') {
//    window.alert('funcionando')
//} else {
//    window.alert('jquery necessita ser carregado...')
//}