from . import views

from django.conf.urls import url

app_name = 'accounts'
urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^mypage/$', views.MypageView.as_view(), name='mypage'),
]
