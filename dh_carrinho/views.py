#-*- coding: utf-8 -*-
from dh_carrinho.negocio import Carrinho, ItemCarrinho, get_carrinho
from django.views.generic import View, TemplateView
from django.http import  HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
OPERACOES = (u'a', u'd', u'r',)#aumentar quantidade, diminuir quantidade, remover item
class CarrinhoView(View):
    def get(*args, **kwargs):
        return HttpResponseForbidden()
    def post(self, request, *args, **kwargs):
        if request.is_ajax():

            carrinho = get_carrinho(request)
            operacao = request.POST.get(u'operacao', None)
            pk_item = None
            try:
                pk_item = int(request.POST[u'item'])
            except:
                pass
            if operacao not in OPERACOES or pk_item is None:
                return HttpResponseForbidden()
        
            if operacao == u'a':
                carrinho.aumenta_quantidade(pk_item)
            elif operacao == u'd':
                carrinho.diminui_quantidade(pk_item)
            elif operacao == u'r':
                carrinho.deleta_item(pk_item)
            request.session[u'carrinho'] = carrinho
            return HttpResponse('ok')
        else:
            return HttpResponseForbidden()

class ListaAtualView(View):

    def get(self, request, *args, **kwargs):
        carrinho = get_carrinho(request)
        return render_to_response(settings.DH_CARRINHO_TEMPLATE_CARRINHO, 
                                  RequestContext(request, 
                                                 {u'carrinho': carrinho}))

    def post(*args, **kwargs):
        return HttpResponseForbidden()


class PaginaCarrinhoView(TemplateView):
    """
    View para ser utilizada pelos projetos na renderização da página que
    mostra o carrinho completo, e que se premite alterar quantidades, remover
    itens, etc.
    """

    def get_context_data(self, **kwargs):
        context = super(PaginaCarrinhoView, self).get_context_data(**kwargs)
        context[u'carrinho'] = get_carrinho(self.request)
        return context

    def post(self, request, *args, **kwargs):
        carrinho = get_carrinho(request)
        operacao = request.POST.get(u'operacao', None)
        pk_item = None
        try:
            pk_item = int(request.POST[u'item'])
        except:
            return HttpResponseForbidden()
        if operacao == u'altera_quantidade':
            try:
                quantidade = int(request.POST[u'quantidade'])
            except:
                return HttpResponseForbidden()
            carrinho.altera_quantidade(pk_item, quantidade)
            request.session[u'carrinho'] = carrinho
            #redirect para a mesma pagina
            return HttpResponseRedirect(request.path)
        elif operacao == u'apaga_item':
            carrinho.deleta_item(pk_item)
            request.session[u'carrinho'] = carrinho
            #redirect para a mesma pagina
            return HttpResponseRedirect(request.path)
        else:
            return HttpResponseForbidden()