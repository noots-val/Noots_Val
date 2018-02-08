from django.conf.urls import url
from . import views

app_name = 'official_site'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^products/', views.products, name='products'),
    url(r'^contact/', views.contact, name='contact'),
]
