from django.conf.urls import url
from .views import EcIndexListView
from .views import EcCommodityDetailView
from .views import EcCartListView
from .views import EcPaymentListView
from .views import EcPaymentCompleteTemplateView

from . import views

app_name = 'portfolio'
urlpatterns = [
    url(r'^index/$', EcIndexListView.as_view(), name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', EcCommodityDetailView.as_view(), name='detail'),
    url(r'^cart/$', EcCartListView.as_view(), name='cart'),
    url(r'^payment/$', EcPaymentListView.as_view(), name='payment'),
    url(r'^payment_complete/$', EcPaymentCompleteTemplateView.as_view(), name='payment_complete'),
]
