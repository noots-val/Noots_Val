from django.views.generic import TemplateView
# from portfolio.models import portfoliomodel 後でモデル追加


class EcIndexTemplateView(TemplateView):
    template_name = "portfolio/ec_index.html"
