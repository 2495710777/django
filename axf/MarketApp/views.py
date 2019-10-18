from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods
from MarketApp.view_helper import ORDER_RULE_DEFAULT, ORDER_RULE_NUM_DESC, ORDER_RULE_NUM_ASC, ORDER_RULE_PRICE_DESC, \
    ORDER_RULE_PRICE_ASC


def market(request):
    typeid = request.GET.get('typeid', '104749')
    # print(type(typeid))
    # print(typeid)
    foodtypes = AxfFoodType.objects.all()

    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames
    # print(childtypenames)

    childtype_list = childtypenames.split('#')
    # print(childtype_list)

    typename_list = []
    for childtype in childtype_list:
        typename = childtype.split(':')
        typename_list.append(typename)
    # print(typename)

    hotfoods = AxfGoods.objects.filter(categoryid=typeid)
    # 二级联动查询
    childcid = request.GET.get('childcid', '0')

    if childcid and childcid != '0':
        hotfoods = hotfoods.filter(childcid=childcid)


    # if childcid == '0':
    #     pass
    # else:
    #     hotfoods = hotfoods.filter(childcid=childcid)

    sort_lists = [
        ['综合排序', ORDER_RULE_DEFAULT],
        ['价格升序', ORDER_RULE_PRICE_ASC],
        ['价格降序', ORDER_RULE_PRICE_DESC],
        ['销量升序', ORDER_RULE_NUM_ASC],
        ['销量降序', ORDER_RULE_NUM_DESC]
    ]

    # 三级联动查询
    price_sort = request.GET.get('price_sort', ORDER_RULE_DEFAULT)
    if price_sort == ORDER_RULE_PRICE_ASC:
        hotfoods = hotfoods.order_by('price')
    elif price_sort == ORDER_RULE_PRICE_DESC:
        hotfoods = hotfoods.order_by('-price')
    elif price_sort == ORDER_RULE_NUM_ASC:
        hotfoods = hotfoods.order_by('productnum')
    elif price_sort == ORDER_RULE_NUM_DESC:
        hotfoods = hotfoods.order_by('-productnum')

    allgoods = AxfGoods.objects.all()

    context = {
        'foodtypes': foodtypes,
        'allgoods': allgoods,
        'typeid': typeid,
        'childcid': childcid,
        'price_sort': price_sort,
        'sort_lists': sort_lists,
        'hotfoods': hotfoods,
        'typename_list': typename_list
    }
    return render(request, 'axf/main/market/market.html', context=context)
