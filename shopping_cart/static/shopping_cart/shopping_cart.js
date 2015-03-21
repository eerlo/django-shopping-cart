function trigger_apos_atualizar_carrinho(){
}

function atualiza_div_carrinho(item_adicionado, operacao, produto){
    $.ajax({
        type: "GET",
        url: '/carrinho/lista/',
        success: function(retorno){
                    $('#carrinho').html(retorno);
                    if(item_adicionado){
                        trigger_apos_atualizar_carrinho(operacao, produto);
                    }
                 }
    });
}

$(document).on("submit", "form.manipulacao-carrinho",
    function(){
        produto = $(this).find('input[name=item]:eq(0)').val();
        token = $(this).find('input[name=csrfmiddlewaretoken]:eq(0)').val();
        operacao = $(this).find('input[name=operacao]:eq(0)').val();
        $.ajax({
            type: "POST",
            url: '/carrinho/',
            data: {"operacao": operacao,
                   "item": produto,
                   "csrfmiddlewaretoken": token},
            success: function(){
                        atualiza_div_carrinho(true, operacao, produto);
                     }
        });
        return false;
    }
);

atualiza_div_carrinho(false, false, false);