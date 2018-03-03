from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import Commodity
from .models import Cart

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
        request_get = self.request.GET
        if "query_param" in request_get:
            return Commodity.objects.filter(category=request_get.get("category"))
        else:
            return Commodity.objects.all()


class EcCommodityDetailView(DetailView):
    """
    ECサイトのポートフォリオのdetailへと画面遷移するためのクラス
    """

    model = Commodity
    template_name = "portfolio/ec_commodity.html"


class EcCartListView(ListView):
    """
    ECサイトのポートフォリオのcartへと画面遷移するためのクラス
    """

    model = Cart
    template_name = "portfolio/ec_cart.html"

    def get_queryset(self):
        return Cart.objects.select_related("commodity", "user").filter(user__id=1)


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
