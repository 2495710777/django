from django.conf.urls import url

from OrderApp import views

urlpatterns = [
    url(r'^order_detail/', views.order_detail, name='order_detail'),
    url(r'^make_order/', views.make_order, name='make_order'),

    # 支付接口
    url(r'^alipay/', views.alipay, name='alipay'),
]
