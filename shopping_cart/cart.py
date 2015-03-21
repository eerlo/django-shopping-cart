#-*- coding: utf-8 -*-

from django.db.models import get_model

from shopping_cart.config import PRODUCT_MODEL


class CartItem(object):
    """
    Representa um item do Cart
    """
    def __init__(self, item_pk, quantity):
        """
        Guarda o id do item e a quantity
        """
        self.item_pk = item_pk
        self.quantity = quantity

    def get_object(self):
        try:
            return PRODUCT_MODEL.objects.get(pk=self.item_pk)
        except PRODUCT_MODEL.DoesNotExist:
            return None

class Cart(object):
    """
    Representa o carrinho de um usuário
    """
    def __init__(self):
        self.items = []

    def get_item(self, item_pk):
        for item in self.items:
            if item.item_pk == item_pk:
                return item

    def get_or_create_item(self, item_pk):
        for item in self.items:
            if item.item_pk == item_pk:
                return item
        new_item = ItemCarrinho(item_pk, 0)
        self.items.append(new_item)
        return new_item

    def change_quantity(self, item_pk, quantity):
        self.get_item(item_pk).quantity = quantity

    def increase_quantity(self, item_pk):
        self.get_or_create_item(item_pk).quantity += 1

    def decrease_quantity(self, item_pk):
        if self.get_item(item_pk).quantity > 0:
            self.get_item(item_pk).quantity -= 1

        if self.get_item(item_pk).quantity == 0:
            self.delete_item(item_pk)

    def delete_item(self, item_pk):
        self.items.remove(self.get_item(item_pk))

    def erase_cart(self):
        self.items = []

    def get_quantity_total_items(self):
        return sum([item.quantity for item in self.items])

def get_cart(request):
    return request.session.get(u'cart', Carrinho())
