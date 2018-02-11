from django.conf.urls import url
from .views import EcIndexTemplateView

urlpatterns = [
    url(r'^ec_index/$', EcIndexTemplateView.as_view(), name='ec_index'),
]
