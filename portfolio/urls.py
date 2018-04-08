from django.conf.urls import url
from .views import *

app_name = 'portfolio'
urlpatterns = [
    url(r'^index/$', EcIndexListView.as_view(), name='index'),
    url(r'^detail/(?P<pk>[0-9]+)/$', EcProductDetailView.as_view(), name='detail'),
    url(r'^cart/$', EcCartListView.as_view(), name='cart'),
    url(r'^payment/$', EcPaymentListView.as_view(), name='payment'),
    url(r'^payment_complete/$', EcPaymentCompleteTemplateView.as_view(), name='payment_complete'),
    url(r'^add_product/', AddProductView.as_view(), name='add_product'),
    url(r'^delete_cart/', DeleteCartView.as_view(), name='delete_cart'),
]
