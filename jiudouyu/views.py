from django.shortcuts import render, render_to_response, redirect

from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import *
from .response import *
from .validate import *
from .models import CurrentAccount
from django.utils import timezone
from django.db.models import *
from django.core.cache import cache
import datetime, json
from django.db.models import Q

def request_test(request):
    data = {}
    data['scheme'] = request.scheme
    data['body'] = request.body.decode('utf-8')
    data['path'] = request.path
    data['path_info'] = request.path_info
    data['method'] = request.method
    data['encoding'] = request.encoding
    data['content_type'] = request.content_type
    data['content_params'] = request.content_params
    data['get'] = request.GET
    data['post'] = request.POST
    data['cookies'] = request.COOKIES
    data['files'] = request.FILES
    data['remote_host'] = request.META.get('REMOTE_HOST')
    data['remote_addr'] = request.META.get('REMOTE_ADDR')
    data['server_name'] = request.META.get('SERVER_NAME')
    data['server_port'] = request.META.get('SERVER_PORT')
    data['user_agent'] = request.META.get('HTTP_USER_AGENT')
    data['is_secure'] = request.is_secure()
    data['is_ajax'] = request.is_ajax()

    cache.set('abc', 'afdsf')
    return JsonResponse(call_success(data))

def index(request):
    now = timezone.now()
    register_count = User.objects.count()

    # select count(id) as register_count from core_user
    registe_data = User.objects.aggregate(register_count=Count('id'))

    # select sum(cash) as current_amount from core_current_account
    current_data = CurrentAccount.objects.aggregate(current_amount = Sum('cash'))

    data = {
        'registe_count': registe_data['register_count'],
        'current_invest_amount': current_data['current_amount'],
        'time': now.strftime('%Y-%m-%d %H:%M:%S')
    }

    # select distinct(status_code) from core_user
    status_list = User.objects.all().values('status_code').distinct()
    for status in status_list:
        print(status['status_code'])

    # select sum(cash) as invest_amount from core_invest where user_id = 82692
    user_invest = Invest.objects.filter(user_id=82692).aggregate(invest_amount=Sum('cash'))

    # select user_id, sum(cash) as invest_amount from core_invest order by invest_amount desc limit 10
    top10_invest_list = Invest.objects.values('user_id').annotate(invest_amount=Sum('cash')).order_by('-invest_amount')[:10]

    for list in top10_invest_list:
        print(list['user_id'], list['invest_amount'])

    cache.set('name', 'zhangshuang')

    return JsonResponse(call_success(data))


def user_list(request):

    # select id, identity_card, phone, balance, real_name, created_at from core_user where real_name <> '' order by id desc limit 20
    user = User.objects.values('identity_card', 'phone', 'balance', 'real_name', 'created_at', 'id').exclude(real_name='').order_by('-id')[:20]
    return render(request, 'list.html', {'user_list': user})

def user_info(request, user_id):
    # select * from core_user where id = <user_id>
    user = User.objects.get(id=user_id)
    return render(request, 'info.html', {'user': user})

def edit_name(request):
    user_id = request.POST.get('user_id')
    name = request.POST.get('name')

    # 判断用户是否存在
    User.objects.filter(id=0).exists()
    # update core_user set real_name= <name> where id = <user_id>
    User.objects.filter(id=user_id).update(real_name=name)
    return JsonResponse(call_success({'user_id': user_id, 'msg': '修改姓名成功'}))


def delete_user(request, user_id):
    # delete from core_user where id = <user_id>
    User.objects.filter(id=user_id).delete()
    return JsonResponse(call_success({'user_id': user_id, 'msg': '删除用户成功'}))


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        import hashlib
        password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()

        try:
            user = User()
            user.phone = phone
            user.password_hash = password_hash
            user.save()
            # insert into core_user(phone, password_hash) values(<phone>, <password_hash>)
        except Exception as e:
            print(e)
            return JsonResponse(call_error('注册失败'))

        result = call_success({'user_id': user.id})
        return JsonResponse(result)

def identify(request, user_id):
    print(request.GET,request.POST)
    return HttpResponse("实名认证")


def orm_test(request):
    # select * from core_user where id > 1000 and balance > 1000.0 limit 10
    user = User.objects.filter(balance__gt=1000.0, id__gt=1000)[:10]

    # select * from core_user where created_at > '2017-01-01 00:00:00' order by id desc limit 10
    user = User.objects.filter(created_at__gt = datetime.datetime(2017, 1, 1)).order_by('-id')[:10]

    # select * from core_user where status_code in (100, 200) limit 10
    user = User.objects.filter(status_code__in=[100, 200])[:10]

    # select core_current_account where user_id = 82692 or cash > 100000.0
    current_user = CurrentAccount.objects.filter(Q(user_id=82692) | Q(cash__gt=10000.0))[:10]

    # select count(id) from core_current_account where user_id = 82692 or cash > 100000.0
    current_user = CurrentAccount.objects.filter(Q(user_id=82692) | Q(cash__gt=10000.0)).aggregate(mycount=Count('id'))

    # raw sql
    user = User.objects.raw("select id, phone from core_user where id in (14, 82692, 10000)")
    user = User.objects.raw("select u.id, u.phone, sum(cash) as total_invest from core_user as u, core_invest as i where u.id = i.user_id and u.id = %s", [82692])