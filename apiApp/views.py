from django.shortcuts import render
from django.http import JsonResponse
from apiApp.coineoneApi import CoinoneApi
from apiApp.apiDataProcessing import V2ApiProcessing
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt

TOKEN = '<your coinone api token>'
KEY = '<your coinone api key>'
c = CoinoneApi(token=TOKEN, key=KEY)

def coinlist(request):
    if request.method == "GET":
        if cache.get("coinlist") == None:
            data = c.get_response('v2/account/balance/', c.get_base_payload())
            v2 = V2ApiProcessing();
            balance = v2.get_coin_list(data)
            cache.set("coinlist",balance)
            return JsonResponse(data=balance)
        else:
            return JsonResponse(cache.get("coinlist"))

def balance(request):
    if request.method == "GET":
        if cache.get("balance") == None:
            data = c.get_response('v2/account/balance/', c.get_base_payload())
            cache.set("balance",data)
            return JsonResponse(data=data)
        else:
            return JsonResponse(cache.get("balance"))

def userinfo(request):
    if request.method == "GET":
        if cache.get("userinfo") == None:
            data = c.get_response('v2/account/user_info/', c.get_base_payload())
            cache.set("userinfo",data)
            return JsonResponse(data=data)
        else:
            return JsonResponse(cache.get("userinfo"))

def deposit(request):
    if request.method == "GET":
        if cache.get("deposit") == None:
            data = c.get_response('v2/account/deposit_address/', c.get_base_payload())
            cache.set("deposit",data)
            return JsonResponse(data=data)
        else:
            return JsonResponse(cache.get("deposit"))


def limitsell(request, currency, price, qty):
    if request.method == "GET":
        data = c.get_response('v2/order/limit_sell/', c.create_payload({
                    'price': price,
                    'qty': qty,
                    'currency': currency,
                }))
        return JsonResponse(data=data)

def limitbuy(request, currency, price, qty):
    if request.method == "GET":
        data = c.get_response('v2/order/limit_buy/', c.create_payload({
                    'price': price,
                    'qty': qty,
                    'currency': currency,
                }))
        return JsonResponse(data=data)
