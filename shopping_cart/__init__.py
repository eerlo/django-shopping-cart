#-*- coding: utf-8 -*-
from django.conf import settings
from django.db.models import get_model
MODEL_PRODUTO = get_model(*settings.DH_CARRINHO_MODEL_PRODUTO.split(u'.'))