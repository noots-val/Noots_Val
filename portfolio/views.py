from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product
from .models import Cart

"""
ポートフォリオのviews
"""
__author__ = "Noots"


class EcIndexListView(ListView):
    """
    ECサイトのポートフォリオのindexへと画面遷移するためのクラス
    """

    model = Product
    template_name = "portfolio/index.html"

    def get_queryset(self):
        """
        URLパラメータの処理メソッド
        :return: categoryパラメータによってフィルタされたProductオブジェクト（パラメータが空なら全件取得）
        """
        request_get = self.request.GET
        if "query_param" in request_get:
            return Product.objects.filter(category=request_get.get("category"))
        else:
            return Product.objects.all()


class EcProductDetailView(DetailView):
    """
    ECサイトのポートフォリオのdetailへと画面遷移するためのクラス
    """

    model = Product
    template_name = "portfolio/detail.html"


class EcCartListView(LoginRequiredMixin, ListView):
    """
    ECサイトのポートフォリオのcartへと画面遷移するためのクラス
    """

    model = Cart
    template_name = "portfolio/cart.html"

    def get_queryset(self):
        """
        カートの中身をフィルタするメソッド
        :return: ユーザーIDでフィルタしたカートのProduct
        """
        return Cart.objects.select_related("product", "user").filter(user__id=self.request.user.id)


class EcPaymentListView(LoginRequiredMixin, ListView):
    """
    ECサイトのポートフォリオのpaymentへと画面遷移するためのクラス
    """

    model = Cart
    template_name = "portfolio/payment.html"

    def get_queryset(self):
        """
        カートの中身をフィルタするメソッド
        :return: ユーザーIDでフィルタしたカートのproduct
        """
        return Cart.objects.select_related("product", "user").filter(user__id=self.request.user.id)

    def get_context_data(self, **kwargs):
        cart_of_user = self.get_queryset()

        context = super().get_context_data(**kwargs)
        prices_of_every_commodities = [prices_and_amounts["product__price"] * prices_and_amounts["amount"] for
                                       prices_and_amounts in
                                       cart_of_user.values("product__price", "amount")]
        merchandise_total = sum(prices_of_every_commodities)
        context["merchandise_total"] = merchandise_total
        return context


class EcPaymentCompleteTemplateView(LoginRequiredMixin, TemplateView):
    """
    ECサイトのポートフォリオのpayment_completeへと画面遷移するためのクラス
    """

    template_name = "portfolio/payment_complete.html"


class AddProductView(LoginRequiredMixin, TemplateView):
    model = Cart
    template_name = "portfolio/index.html"

    def get_queryset(self):
        """
        動かないメソッド
        idなどは直接データを入れるのではなく、リレーションテーブルのオブジェクトを入れるらしい
        :return:
        """
        user_id = self.request.user.id
        product_id = self.request.GET.get('id')
        amount = self.request.GET.get('amount')
        cart = Cart(user=user_id, product=Product(id=product_id), amount=amount)
        cart.save()
        return cart


class DeleteCartView(LoginRequiredMixin, TemplateView):
    model = Cart
    template_name = "portfolio/index.html"

    def get_queryset(self):
        """
        動かないメソッド
        idなどは直接データを入れるのではなく、リレーションテーブルのオブジェクトを入れるらしい
        :return:
        """
        user = User.objects.get(pk=self.request.user.id)
        cart = Cart(user=user)
        cart.delete()
