from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response

from rest_framework.decorators import detail_route
import base64
import argparse

from google.cloud import translate
import six

from traductor.serializers import TextoSerializer
from django.http import JsonResponse, HttpResponse



class TraductorViewSet(viewsets.ModelViewSet):


    @detail_route(methods=['post'])

    def set_translate(self, request):
# Recovery data POST fields for send api translate
        posti = request.data
        palabras = posti['palabras']
        print (posti)
        target='en'
        fintext = translate_text_with_model(target, palabras, model=translate.NMT)
        print (fintext)
        return HttpResponse(translate_text_with_model(target, palabras, model=translate.NMT), status=201)

    @detail_route(methods=['get'])

    def receive_tra(self, request):
        print(request.data)
        geti = request.GET.get('palabras')
        print (geti)
        #palabras = geti['palabras']
        print (geti)
        target='en'
        fintext = translate_text_with_model(target, geti, model=translate.NMT)
        print (fintext)
        return HttpResponse(translate_text_with_model(target, geti, model=translate.NMT), status=201)

def translate_text_with_model(target, text, model):
    """Translates text into the target language.
    Make sure your project is whitelisted.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target, model=model)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))
    responser = "{'Palabras':[{'resultado':'"
    responsery = format(result['translatedText'])
    responserz = "'}]}"
    todotranslate = (responser + responsery + responserz)
    print (todotranslate)
    return todotranslate

'''
    @detail_route(methods=['get'])
    def show(self, request):
        texto = request.data
        print(texto)
'''