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
        """
        カートの中身をフィルタするメソッド
        :return: ユーザーIDでフィルタしたカートのCommodity（後程ユーザー関連の処理はまとめて実装）
        """
        return Cart.objects.select_related("commodity", "user").filter(user__id=1)


class EcPaymentListView(ListView):
    """
    ECサイトのポートフォリオのpaymentへと画面遷移するためのクラス
    """

    model = Cart
    template_name = "portfolio/ec_payment.html"

    cart_of_user = Cart.objects.select_related("commodity", "user").filter(user__id=1)

    def get_queryset(self):
        """
        カートの中身をフィルタするメソッド
        :return: ユーザーIDでフィルタしたカートのCommodity（後程ユーザー関連の処理はまとめて実装）
        """
        return self.cart_of_user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prices_of_every_commodities = [prices_and_amounts["commodity__price"] * prices_and_amounts["amount"] for
                                       prices_and_amounts in
                                       self.cart_of_user.values("commodity__price", "amount")]
        merchandise_total = sum(prices_of_every_commodities)
        context["merchandise_total"] = merchandise_total
        return context


class EcPaymentCompleteTemplateView(TemplateView):
    """
    ECサイトのポートフォリオのpayment_completeへと画面遷移するためのクラス
    """

    template_name = "portfolio/ec_payment_complete.html"
