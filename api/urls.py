# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import TraductorViewSet

translate_creationp = TraductorViewSet.as_view({
    'post': 'set_translate'
})

translate_creation = TraductorViewSet.as_view({
    'get': 'receive_tra'
})

urlpatterns = [
    url(r'^v1/traductor$', translate_creationp,
        name='translate_creationp'),
    url(r'^v1/traductor/$', translate_creation,
        name='translate_creation'),
]