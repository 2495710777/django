import re
import uuid

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.utils.six import BytesIO
from django.views.decorators.csrf import csrf_exempt

from UserApp.models import AxfUser
from UserApp.view_constaint import send_email
from axf import settings


@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request, 'axf/user/register/register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        icon = request.FILES.get('icon')

        password = make_password(password)

        user = AxfUser()

        user.u_name = name
        user.u_email = email
        user.u_password = password
        user.u_icon = icon

        token = uuid.uuid4()
        user.u_token = token
        user.save()

        cache.set(token, user.id, timeout=45)

        send_email(name, email, token)

        return render(request, 'axf/user/login/login.html')


def checkName(request):
    name = request.GET.get('name')
    users = AxfUser.objects.filter(u_name=name)
    data = {
        'msg': '√用户名可以使用',
        'status': 200
    }
    if users.count() > 0:
        data['msg'] = '×用户名已经存在'
        data['status'] = 201
    return JsonResponse(data=data)


def testmail(request):
    return HttpResponse('send success')


def activeAccount(request):
    # 通过点击激活获取的请求参数
    token = request.GET.get('token')

    user_id = cache.get(token)

    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        user.u_active = 1
        user.save()
        cache.delete(token)
        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件已过期')

    # users = AxfUser.objects.filter(u_token=token)
    # if users.exists():
    #     user = users.first()
    #     user.u_active = 1
    #     user.save()
    #     return HttpResponse('激活成功')
    # else:
    #     return HttpResponse('邮件已过期')


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'axf/user/login/login.html')
    if request.method == 'POST':
        # 用户输入的验证码
        imgcode = request.POST.get('imgcode').strip()
        # 所有的验证码生成策略都会把验证码绑定到session上
        verify_code = request.session.get('verify_code')

        b = re.search(imgcode, verify_code, re.IGNORECASE)
        print(b)
        if b:
            name = request.POST.get('name')

            users = AxfUser.objects.filter(u_name=name)
            if users.count() > 0:
                user = users.first()
                password = request.POST.get('password')
                if check_password(password, user.u_password):
                    if user.u_active:
                        request.session['user_id'] = user.id
                        request.session['token'] = user.u_token
                        return redirect(reverse('axfmine:mine'))
                    else:
                        error = '账号未激活'
                        return render(request, 'axf/user/login/login.html', context=locals())

                else:
                    error = '用户名或者密码输入错误'
                    return render(request, 'axf/user/login/login.html', context=locals())

            else:
                error = '用户名或者密码输入错误'
                return render(request, 'axf/user/login/login.html', context=locals())
        else:
            error = '验证码错误'
            return render(request, 'axf/user/login/login.html', context=locals())


def get_code(request):
    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


