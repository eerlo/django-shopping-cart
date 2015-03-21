function cart_after_updated_trigger(){ }
function cart_before_updated_trigger(){ }

function update_cart(has_update, cart_action, product){
    $.ajax({
        type: "GET",
        url: '/shopping-cart/list/',
        success: function(data){
            $('#cart').html(data);
            if(has_update){
                cart_after_updated_trigger(cart_action, product);
            }
         }
    });
}

$(document).on("submit", "form.cart-manipulation",
    function(){
        product = $(this).find('input[name=item]:eq(0)').val();
        token = $(this).find('input[name=csrfmiddlewaretoken]:eq(0)').val();
        cart_action = $(this).find('input[name=cart_action]:eq(0)').val();

        $.ajax({
            type: "POST",
            url: '/shopping-cart/',
            data: {"cart-action": cart_action,
                "item": product,
                "csrfmiddlewaretoken": token
            },
            success: function(){
                update_cart(true, cart_action, product);
            }
        });
        return false;
    }
);

update_cart(false, false, false);
