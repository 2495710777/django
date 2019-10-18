from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from CartApp.models import AxfCart
from MarketApp.models import AxfGoods


def cart(request):
    # user_id = request.session.get('user_id')
    user = request.user
    carts = AxfCart.objects.filter(c_user_id=user.id)
    is_all_select = not AxfCart.objects.filter(c_is_select=False).filter(c_user_id=user.id).exists()
    context = {
        'carts': carts,
        'total_price': get_total_price(user.id),
        'is_all_select': is_all_select
    }
    return render(request, 'axf/main/cart/cart.html', context=context)


def get_total_price(user_id):
    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)
    total_price = 0
    for cart in carts:
        total_price = total_price + cart.c_goods.price * cart.c_goods_num
    return '%.2f' % total_price


def addToCart(request):
    # user_id = request.session.get('user_id')
    data = {
        'msg': 'ok',
        'status': 200
    }
# 获取中间件中设置的request.user
    user = request.user
#     print(user)
#     if user_id:
    goodsid = request.GET.get('goodsid')
    carts = AxfCart.objects.filter(c_user_id=user.id).filter(c_goods_id=goodsid)
    if carts.count() > 0:
        cart = carts.first()
        cart.c_goods_num = cart.c_goods_num + 1

    else:
        cart = AxfCart()
        cart.c_goods_id = goodsid
        cart.c_user_id = user.id
    cart.save()
    data['c_goods_num'] = cart.c_goods_num
    return JsonResponse(data=data)
    # else:
    #     data['msg'] = '未登录'
    #     data['status'] = 201
    #     return JsonResponse(data=data)

def subToCart(request):
    # user_id = request.session.get('user_id')
    data = {
        'msg': 'ok',
        'status': 200
    }

    user = request.user
    print(user)
    # if user_id:
    goodsid = request.GET.get('goodsid')
    carts = AxfCart.objects.filter(c_user=user).filter(c_goods_id=goodsid)
    print(carts.count())
    if carts.count() > 0:
        cart = carts.first()
        if cart.c_goods_num > 1:
            cart.c_goods_num = cart.c_goods_num - 1
            data['c_goods_num'] = cart.c_goods_num
            cart.save()
        else:
            cart.c_goods_num = 0
            data['c_goods_num'] = cart.c_goods_num
            cart.delete()
    else:
        data['c_goods_num'] = 0
    return JsonResponse(data=data)
    # else:
    #     data['msg'] = '未登录'
    #     data['status'] = 201
    # return JsonResponse(data=data)



@csrf_exempt
def addCart(request):
    data = {
        'msg': 'ok',
        'status': 200
    }
    cart_id = request.POST.get('cart_id')
    cart = AxfCart.objects.get(pk=cart_id)
    cart.c_goods_num = cart.c_goods_num + 1
    cart.save()
    data['c_goods_num'] = cart.c_goods_num

    # user_id = request.session.get('user_id')
    # 直接使用request.user对象的属性
    # data['total_price'] = get_total_price(user_id)
    data['total_price'] = get_total_price(request.user.id)
    return JsonResponse(data=data)


@csrf_exempt
def subCart(request):
    data = {
        'msg': 'ok',
        'status': 200
    }

    cart_id = request.POST.get('cart_id')
    cart = AxfCart.objects.get(pk=cart_id)

    if cart.c_goods_num > 1:
        cart.c_goods_num = cart.c_goods_num - 1
        data['c_goods_num'] = cart.c_goods_num
        cart.save()
    else:
        cart.delete()
        data['status'] = 204
    # user_id = request.session.get('user_id')
    # data['total_price'] = get_total_price(user_id)
    data['total_price'] = get_total_price(request.user.id)
    return JsonResponse(data=data)


def changeStatus(request):
    data = {
        'msg': 'ok',
        'status': 200
    }
    cart_id = request.GET.get('cart_id')
    cart = AxfCart.objects.get(pk=cart_id)
    cart.c_is_select = not cart.c_is_select
    cart.save()

    data['c_is_select'] = cart.c_is_select
    user = request.user
    # user_id = request.session.get('user_id')
    is_all_select = not AxfCart.objects.filter(c_is_select=False).filter(c_user=user).exists()
    data['is_all_select'] = is_all_select

    data['total_price'] = get_total_price(user.id)
    return JsonResponse(data=data)


def allSelect(request):
    # user_id = request.session.get('user_id')
    user = request.user
    # print(user)
    cartid_list = request.GET.get('cartid_list')
    cartid_list = cartid_list.split('#')

    carts = AxfCart.objects.filter(id__in=cartid_list)
    data = {
        'msg': 'ok',
        'status': 200,
    }
    for cart in carts:
        cart.c_is_select = not cart.c_is_select
        cart.save()
    data['total_price'] = get_total_price(user.id)
    return JsonResponse(data=data)
