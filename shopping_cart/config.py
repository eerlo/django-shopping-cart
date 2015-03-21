#-*- coding: utf-8 -*-

from django.conf import settings
from django.db.models import get_model

PRODUCT_MODEL = get_model(*settings.SHOPPING_CART_PRODUCT_MODEL.split(u'.'))
