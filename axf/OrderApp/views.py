from alipay import AliPay
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from CartApp.models import AxfCart
from CartApp.views import get_total_price
from OrderApp.models import AxfOrderGoods, AxfOrder
from axf.settings import APP_PRIVATE_KEY_STRING, ALIPAY_PUBLIC_KEY_STRING


def order_detail(request):
    order_id = request.GET.get('order_id')
    order = AxfOrder.objects.get(pk=order_id)
    request.session['order_id'] = order_id
    context = {
        'order': order,
        'total_price': order.axfordergoods_set.first().og_total_price
    }

    return render(request, 'axf/order/order_detail.html', context=context)


def make_order(request):

    user_id = request.session.get('user_id')

    order = AxfOrder()
    order.o_user_id = user_id
    order.save()

    carts = AxfCart.objects.filter(c_is_select=True).filter(c_user_id=user_id)
    for cart in carts:
        orderGoods = AxfOrderGoods()
        orderGoods.og_order = order
        orderGoods.og_goods = cart.c_goods

        orderGoods.og_goods_num = cart.c_goods_num
        orderGoods.og_total_price = get_total_price(user_id)

        orderGoods.save()
        cart.delete()

    data = {
        'msg': 'ok',
        'status': 200,
        'order_id': order.id
    }
    return JsonResponse(data=data)


def alipay(request):
    alipay = AliPay(
        appid="2016101200665392",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=APP_PRIVATE_KEY_STRING,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=ALIPAY_PUBLIC_KEY_STRING,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False  # 默认False
    )

    order_id = request.session.get('order_id')
    order = AxfOrder.objects.get(pk=order_id)

    subject = "爱鲜蜂商品"
    # 电脑网站支付，需要跳转到https://openapi.alipaydev.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单编号
        out_trade_no=order.axfordergoods_set.first().id,
        # 总价
        total_amount=order.axfordergoods_set.first().og_total_price,
        # 商品名
        subject=subject,
        return_url="https://www.1000phone.com",
        notify_url="https://www.1000phone.com"  # 可选, 不填则使用默认notify url
    )

    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)