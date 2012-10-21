#coding:utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),

    # Inclusões mais permissivas devem ficar no final, paa evitar processamento desnecessário
    url(r'', include('eventex.core.urls', namespace='core')),
)

