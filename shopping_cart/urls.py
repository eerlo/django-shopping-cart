from django.conf.urls import patterns, url
from shopping_cart.views import ShoppingCartView, ShoppingCartListView


dh_carrinho_urls = patterns('',
    url(r'^$', ShoppingCartView.as_view(), name='shopping-cart-view'),
    url(r'^list/$', ShoppingCartListView.as_view(),
        name='shopping-cart-list-view'))
