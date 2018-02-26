from django.conf.urls import url
from .views import EcIndexListView
from .views import EcDetailTemplateView
from .views import EcCartTemplateView
from .views import EcPaymentTemplateView
from .views import EcPaymentCompleteTemplateView

app_name = 'portfolio'
urlpatterns = [
    url(r'^ec_index/$', EcIndexListView.as_view(), name='ec_index'),
    url(r'^ec_detail/$', EcDetailTemplateView.as_view(), name='ec_detail'),
    url(r'^ec_cart/$', EcCartTemplateView.as_view(), name='ec_cart'),
    url(r'^ec_payment/$', EcPaymentTemplateView.as_view(), name='ec_payment'),
    url(r'^ec_payment_complete/$', EcPaymentCompleteTemplateView.as_view(), name='ec_payment_complete'),
]
