from django.shortcuts import redirect
from alipay import AliPay
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from Book_Django import settings


@csrf_exempt
def pay(request):
    """开始支付"""
    money=request.POST.get('money')
    amount = int(money)
    trad_no =request.POST.get('order_code')
    alipay = AliPay(
        appid=settings.ALIPAY_APPID,
        app_notify_url='http://127.0.0.1/pay/notify/',
        app_private_key_path=settings.APP_PRIVATE_KEY_PATH,
        alipay_public_key_path=settings.ALIPAY_PUBLIC_KEY_PATH,
        sign_type='RSA2',
        debug=True
    )
    # 生成订单参数
    # 电脑网站的支付地址  https://openapi.alipaydev.com/gateway.do?order_url
    order_url = alipay.api_alipay_trade_page_pay(
        subject='订单',
        out_trade_no=trad_no,
        total_amount=amount,
        return_url='https://127.0.0.1/',  # 支付成功后前端跳转的网址
        notify_url='后台接收支付宝支付相关信息的接口 post请求'
    )
    pay_url = settings.ALT_PAY_DEV_URL + order_url
    return redirect(pay_url)


@csrf_exempt
def notify_callback(request):
    json_data = request.POST.get('sign')
    pass