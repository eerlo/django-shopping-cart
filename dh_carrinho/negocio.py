#-*- coding: utf-8 -*-
from django.db.models import get_model
from dh_carrinho import MODEL_PRODUTO


class ItemCarrinho(object):
    """
    Representa um item do carrinho
    """
    def __init__(self, pk_item, quantidade):
        """
        Guarda o id do item e a quantidade
        """
        self.pk_item = pk_item
        self.quantidade = quantidade

    def objeto(self):
        try:
            return MODEL_PRODUTO.objects.get(pk=self.pk_item)
        except MODEL_PRODUTO.DoesNotExist:
            return None

class Carrinho(object):
    """
    Representa o carrinho de um usuário
    """
    def __init__(self):
        self.itens = []

    def get_item(self, pk_item):
        for i in self.itens:
            if i.pk_item == pk_item:
                return i

    def get_or_create_item(self, pk_item):
        for i in self.itens:
            if i.pk_item == pk_item:
                return i
        new_item = ItemCarrinho(pk_item, 0)
        self.itens.append(new_item)
        return new_item

    def altera_quantidade(self, pk_item, quantidade):
        self.get_item(pk_item).quantidade = quantidade

    def aumenta_quantidade(self, pk_item):
        self.get_or_create_item(pk_item).quantidade += 1

    def diminui_quantidade(self, pk_item):
        if self.get_item(pk_item).quantidade > 0:
            self.get_item(pk_item).quantidade -= 1
        #se chegamos a 0 deste item, removemos ele
        if self.get_item(pk_item).quantidade == 0:
            self.deleta_item(pk_item)

    def deleta_item(self, pk_item):
        self.itens.remove(self.get_item(pk_item))

    def zera_carrinho(self):
        self.itens = []

    def get_quantidade_total_itens(self):
        return sum([item.quantidade for item in self.itens])

def get_carrinho(request):
    return request.session.get(u'carrinho', Carrinho())