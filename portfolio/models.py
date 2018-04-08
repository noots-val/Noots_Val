from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    # id = AutoField(primary_key=True)  # 自動定義
    product_title = models.CharField(max_length=50)
    image_url = models.URLField()
    category = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    special_flg = models.BooleanField()
    favorite_flg = models.BooleanField()
    description = models.TextField(max_length=1000)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return str(self.pk)


class Cart(models.Model):
    # id = AutoField(primary_key=True)  # 自動定義
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
