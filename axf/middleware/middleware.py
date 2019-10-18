from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from UserApp.models import AxfUser

LOGIN_REQUEST = [
    '/axfcart/cart/'
]

LOGIN_REQUEST_JSON = [
    '/axfcart/addToCart/',
    '/axfcart/subToCart/',
    '/axfcart/addCart/',
    '/axfcart/subCart/',
    '/axfcart/changeStatus/',
    '/axfcart/allSelect/',
]

class LoginMiddleware(MiddlewareMixin):



    def process_request(self,request):
        user_id = request.session.get('user_id')
        if request.path in LOGIN_REQUEST:
            if user_id:
                user = AxfUser.objects.get(pk=user_id)
                request.user = user

            else:
                return redirect(reverse('axfuser:login'))

        if request.path in LOGIN_REQUEST_JSON:

            if user_id:
                user = AxfUser.objects.get(pk=user_id)
                request.user = user
                # data['c_goods_num'] = 0
            else:
                data = {
                    'msg': '未登录',
                    'status': 201
                }
                return JsonResponse(data=data)
