# from app.models import ElasticDemo
import requests
import json
from django.http import JsonResponse
from django.shortcuts import render

# from .documents import *
from .serializers import *

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
    OrderingFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from elasticsearch import RequestsHttpConnection
from elasticsearch import Elasticsearch
# from app.documents import BlogPostIndex

from elasticsearch_dsl.connections import connections

connections.create_connection(hosts = ["localhost"], port="9200", connection_class=RequestsHttpConnection, http_auth=("elastic", "4qrTjXoQ1_4=CAWtlUsI"), use_ssl=True, verify_certs=False)

# Create your views here.
def generate_random_data():
    datas = []
    for news_data in open(r'./News_Category_Dataset_v2.json'):
        datas.append(json.loads(news_data))
    for data in datas:
        ElasticDemo.objects.create(
            title = data.get('headline'),
            content = data.get('short_description')
        )

def index(request):
    generate_random_data()
    return JsonResponse({'status' : 200})

class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    # lookup_field = 'first_name'
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
    
    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
       'title',
        'content',
    )
    filter_fields = {
       'title' : 'title',
        'content' : 'content',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ( 'id'  ,)


