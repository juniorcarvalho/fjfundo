/**
 * Created by junior on 18/10/16.
 */
$(document).ready(function () {
    $("#botao-troca-turma").on("click", function () {
        $.ajax({
            'url': '/turma-seleciona/',
            'success': function (data) {
                $("#lista-turma").html(data);
            }
        });
    })
});
