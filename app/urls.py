from django.urls import path
from app.views import index, PublisherDocumentView

app_name = "application"
urlpatterns = [
    path('insert_data/', index, name='insert_data'),
    path('search/' , PublisherDocumentView.as_view({'get': 'list'})),
]
