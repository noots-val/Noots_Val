from django.db import models


class Commodity(models.Model):
    # id = AutoField(primary_key=True)  # 自動定義
    commodity_title = models.CharField(max_length=50)
    image_url = models.URLField()
    category = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    special_flg = models.BooleanField()
    favorite_flg = models.BooleanField()
    description = models.TextField(max_length=1000)
    stock = models.PositiveIntegerField()
    recommend1 = models.PositiveIntegerField(null=True)
    recommend2 = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.pk)


class User(models.Model):
    # id = AutoField(primary_key=True)  # 自動定義
    mail_address = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)


class Cart(models.Model):
    # id = AutoField(primary_key=True)  # 自動定義
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
