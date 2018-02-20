from django.db import models


class Commodity(models.Model):
    # id = AutoField(primary_key=True)  # 自動定義
    commodity_title = models.CharField(max_length=50)
    image_url = models.URLField
    category = models.CharField(max_length=20)
    price = models.PositiveIntegerField
    special_flg = models.BooleanField
    favorite_flg = models.BooleanField
    description = models.TextField
    recommend1 = models.PositiveIntegerField(null=True)
    recommend2 = models.PositiveIntegerField(null=True)