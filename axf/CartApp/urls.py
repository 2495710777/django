from django.conf.urls import url

from CartApp import views

urlpatterns = [
    url(r'^cart/', views.cart, name='cart'),
    # 添加闪购商品到购物车
    url(r'^addToCart/', views.addToCart, name='addToCart'),
    #　购物车商品数量减少
    url(r'^subToCart/', views.subToCart, name='subToCart'),

    url(r'^addCart/', views.addCart, name='addCart'),
    url(r'^subCart/', views.subCart, name='subCart'),
    # 购物车商品展示
    # 改变购物车商品的选中状态
    url(r'^changeStatus/', views.changeStatus, name='changeStatus'),
    url(r'^allSelect/', views.allSelect, name='allSelect'),
]