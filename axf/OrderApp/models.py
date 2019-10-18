from django.db import models

# Create your models here.
from MarketApp.models import AxfGoods
from UserApp.models import AxfUser


class AxfOrder(models.Model):
    o_user = models.ForeignKey(AxfUser)

    o_time = models.DateTimeField(auto_now_add=True)
    o_status = models.BooleanField(default=1)

    class Meta:
        db_table = 'order'


class AxfOrderGoods(models.Model):

    og_order = models.ForeignKey(AxfOrder)
    og_goods = models.ForeignKey(AxfGoods)

    # 因为在订单中显示的时候，购物车中的数据已被删除，所以把需要的数据存放到此表中
    og_goods_num = models.IntegerField()
    og_total_price = models.FloatField()

    class Meta:
        db_table = 'ordergoods'