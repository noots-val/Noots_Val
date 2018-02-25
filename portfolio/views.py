from django.views.generic import ListView
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
