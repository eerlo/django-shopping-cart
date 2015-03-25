from django.conf.urls import patterns, url
from shopping_cart import views

from django.views.decorators.csrf import csrf_exempt

shopping_cart_urls = patterns('',
    url(r'^$', csrf_exempt(views.ShoppingCartView.as_view()),
        name='shopping-cart-view'),
    url(r'^list/$', views.ShoppingCartListView.as_view(),
        name='shopping-cart-list-view'),
    url(r'^detail/$', views.ShoppingCartListDetailView.as_view(),
        name='shopping-cart-detail-view')
)
