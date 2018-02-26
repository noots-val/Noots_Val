from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Commodity

"""
ポートフォリオのviews
"""
__author__ = "Noots"


class EcIndexListView(ListView):
    """
    ECサイトのポートフォリオのindexへと画面遷移するためのクラス
    """

    model = Commodity
    template_name = "portfolio/ec_index.html"

    def get_queryset(self):
        """
        URLパラメータの処理メソッド
        :return: categoryパラメータによってフィルタされたCommodityオブジェクト（パラメータが空なら全件取得）
        """
        if "query_param" in self.request.GET:
            category = self.request.GET.get("category")
            return Commodity.objects.filter(category=category)
        else:
            return Commodity.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get("category")
        if category == "None":
            category = ""
        context["category"] = category
        return context


class EcDetailTemplateView(TemplateView):
    """
    ECサイトのポートフォリオのdetailへと画面遷移するためのクラス
    """

    template_name = "portfolio/ec_detail.html"


class EcCartTemplateView(TemplateView):
    """
    ECサイトのポートフォリオのcartへと画面遷移するためのクラス
    """

    template_name = "portfolio/ec_cart.html"


class EcPaymentTemplateView(TemplateView):
    """
    ECサイトのポートフォリオのpaymentへと画面遷移するためのクラス
    """

    template_name = "portfolio/ec_payment.html"


class EcPaymentCompleteTemplateView(TemplateView):
    """
    ECサイトのポートフォリオのpayment_completeへと画面遷移するためのクラス
    """

    template_name = "portfolio/ec_payment_complete.html"
