from django.db import models


# Create your models here.

# INSERT INTO axf_wheel (id, img, name, trackid)
class AxfWheel(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_wheel'


class AxfNav(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_nav'


class AxfMustBuy(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_mustbuy'


class AxfMainShow(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()
    categoryid = models.IntegerField()
    brandname = models.CharField(max_length=64)
    img1 = models.CharField(max_length=256)
    childcid1 = models.IntegerField()
    productid1 = models.IntegerField()
    longname1 = models.CharField(max_length=128)
    price1 = models.IntegerField()
    marketprice1 = models.IntegerField()
    img2 = models.CharField(max_length=256)
    childcid2 = models.IntegerField()
    productid2 = models.IntegerField()
    longname2 = models.CharField(max_length=128)
    price2 = models.IntegerField()
    marketprice2 = models.IntegerField()
    img3 = models.CharField(max_length=256)
    childcid3 = models.IntegerField()
    productid3 = models.IntegerField()
    longname3 = models.CharField(max_length=128)
    price3 = models.IntegerField()
    marketprice3 = models.IntegerField()

    class Meta:
        db_table = 'axf_mainshow'

