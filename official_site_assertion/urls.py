from django.conf.urls import url
from .views import AssertionIndexView

app_name = 'official_site_assertion'
urlpatterns = [
    url(r'^assertion_index$', AssertionIndexView.as_view(), name='assertion_index'),
]
