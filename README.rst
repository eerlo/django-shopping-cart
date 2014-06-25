dh_carrinho
===============

Aplicação de carrinho de compras


INSTALAÇÃO 
------------

Instalar o pacote com "python setup.py install"

Settings
********
Configure o SESSION_SERIALIZER para o PickeSerializer, que consegue serializar objetos python não-primitivos.
SESSION_SERIALIZER = u"django.contrib.sessions.serializers.PickleSerializer"

Configure o SESSION_ENGINE
Recomenda-se utilizar o cache ('django.contrib.sessions.backends.cache'), juntamente com o memcache como backend de cache.
Ou então o signed_cookie, que armazena tudo em cookies criptografados pela SECRET_KEY de seu settings, que é muito importante que seja totalmente confidencial.

Adicione a app.model que deseja-se utilizar como produto.
  ``DH_CARRINHO_MODEL_PRODUTO = 'app.Model'``

Adicione o seu template com a responsabilidade única de mostrar o carrinho.
  ``DH_CARRINHO_TEMPLATE_CARRINHO = u'carrinho.html'``
Este template vai receber como contexto um objeto carrinho, com o nome de carrinho, que possui uma lista chamada itens, e alguns métodos interessantes, como quantidade total de itens.
Cada item da lista é um objeto ItemCarrinho, que possui a pk_item, a quantidade, e alguns métodos interessantes, como o objeto(), que retorna o objeto MODEL configurado no settings, baseado na pk_item daquele ItemCarrinho.


Exemplo de template de carrihno:
<ul>
{% for i in carrinho.itens  %}
    <li>{{ i.quantidade  }} do item {{ i.objeto.nome }}</li>
{% endfor %}
</ul>

Urls
********
  ``from dh_carrinho.urls import dh_carrinho_urls ``
  ``url(r'^carrinho/', include(dh_carrinho_urls),),,``


Utilização:
**********************

Esta aplicação recebe POST na url /carrinho/ com o ID do produto e a operação a ser realizada.

Exemplo para adicionar um produto ao carrinho, para cada item faça isto:

.. code:: django

  <form class="manipulacao-carrinho" action="{% url 'dh_carrinho_view' %}" method="post">
  {% csrf_token %}
    <input type="hidden" name="item" value="{{ objeto.pk }}">
  <input type="hidden" name="operacao" value="a">
  <input type="submit" value="Adicionar">
  </form>


Remover um produto do carrinho:
.. code:: django
    <form class="manipulacao-carrinho" action="{% url 'dh_carrinho_view' %}" method="post">
  {% csrf_token %}
    <input type="hidden" name="item" value="{{ objeto.pk }}">
  <input type="hidden" name="operacao" value="d">
  <input type="submit" value="Remover">
  </form>


OBS: é importante a utilização da class="manipulacao-carrinho", para que funcione os envios ajax.

Esta app requer que se esteja utilizando o jquery no template que utilizar manipulação de carrinho.
No final do template, após o jquery, adicionar o javascript que faz os envios de carrinho e atualiza o carrinho.

.. code:: javascript
<script type="text/javascript" src="{% static 'dh_carrinho/dh_carrinho.js' %}"></script>

Mostrando o carrinho:
**********************
No local one se deseja mostrar o carrinho, basta adicionar um DIV com id="carrinho", que a aplicação automaticamente atualiza a mesma, com o template configurado no setting.


Importante:
***********************
Esta aplicação utiliza a sessão do usuário para armazenar o carrinho de compras, portanto, seja sensato ao cofigurar o backend de session storage em seu projeto Django.
Recomenda-se fortemente o cache como Backend de sessão e o Memcache como backend de cache.