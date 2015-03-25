#-*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render
from django.http import  HttpResponseForbidden, HttpResponse
from django.views.generic import View
from django.template import RequestContext

from shopping_cart.cart import get_cart

class ShoppingCartView(View):

    OPERATIONS = (u'add', u'decrease', u'remove',)

    def _get_item(self, request):
        try:
            return int(request.POST[u'item'])
        except KeyError:
            return HttpResponseForbidden()

    def _get_operation(self, request):
        cart_action = request.POST.get(u'cart-action', None)

        if cart_action not in self.OPERATIONS:
            return HttpResponseForbidden

        return cart_action

    def _do_operation(self, cart, cart_action, item_pk):
        if cart_action == u'add':
            cart.increase_quantity(item_pk)
        elif cart_action == u'decrease':
            cart.decrease_quantity(item_pk)
        elif cart_action == u'remove':
            cart.delete_item(item_pk)

        return cart

    def post(self, request, *args, **kwargs):
        if request.is_ajax():

            cart = get_cart(request)
            cart_action = self._get_operation(request)
            item_pk = self._get_item(request)

            request.session[u'cart'] = self._do_operation(cart, cart_action, item_pk)

            return HttpResponse('Operation Success!')
        else:
            return HttpResponseForbidden()


class ShoppingCartListView(View):

    def get(self, request, *args, **kwargs):
        template_name = kwargs.get('template_name', settings.SHOPPING_CART_TEMPLATE)
        context = {u'cart': get_cart(request)}

        return render(request, template_name, context)

class ShoppingCartListDetailView(ShoppingCartListView):

    def get(self, request, *args, **kwargs):
        kwargs['template_name'] = settings.SHOPPING_CART_DETAIL_TEMPLATE
        return super(ShoppingCartListDetailView, self).get(request, *args, **kwargs)
