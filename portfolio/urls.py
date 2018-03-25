from django.conf.urls import url
from .views import EcIndexListView
from .views import EcCommodityDetailView
from .views import EcCartListView
from .views import EcPaymentListView
from .views import EcPaymentCompleteTemplateView

from . import views

app_name = 'portfolio'
urlpatterns = [
    url(r'^ec_index/$', EcIndexListView.as_view(), name='ec_index'),
    url(r'^ec_detail/(?P<pk>[0-9]+)/$', EcCommodityDetailView.as_view(), name='ec_detail'),
    url(r'^ec_cart/$', EcCartListView.as_view(), name='ec_cart'),
    url(r'^ec_payment/$', EcPaymentListView.as_view(), name='ec_payment'),
    url(r'^ec_payment_complete/$', EcPaymentCompleteTemplateView.as_view(), name='ec_payment_complete'),
]
