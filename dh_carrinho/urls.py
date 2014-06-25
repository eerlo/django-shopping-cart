from django.conf.urls import patterns, url
from dh_carrinho.views import CarrinhoView, ListaAtualView


dh_carrinho_urls = patterns('',
                       url(r'^$',
                           CarrinhoView.as_view(),
                           name='dh_carrinho_view'),

                       url(r'^lista/$',
                           ListaAtualView.as_view(),
                           name='dh_carrinho_lista_view'),

                       )
