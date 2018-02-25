from django.conf.urls import url
from .views import EcIndexListView

app_name = 'portfolio'
urlpatterns = [
    url(r'^ec_index/$', EcIndexListView.as_view(), name='ec_index'),
]
