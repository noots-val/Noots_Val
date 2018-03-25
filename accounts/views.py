from .forms import RegisterForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class MypageView(TemplateView):
    template_name = 'accounts/mypage.html'
