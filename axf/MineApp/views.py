from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from UserApp.models import AxfUser


def mine(request):
    user_id = request.session.get('user_id', '未登录')

    if user_id != '未登录':
        # usertoken = request.session.get('token')
        user = AxfUser.objects.filter(id=user_id)[0]
        context = {
            'username': user.u_name,
            'icon': user.u_icon
        }
        return render(request, 'axf/main/mine/mine.html', context=context)
    else:
        context = {
            'username': user_id
        }
        return render(request, 'axf/main/mine/mine.html', context=context)


def logout(request):
    request.session.flush()
    context = {
        'username': '未登录'
    }
    return render(request, 'axf/main/mine/mine.html', context=context)