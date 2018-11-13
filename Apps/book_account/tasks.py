from random import Random
from django.core.mail import send_mail
from Apps.book_main.models import EmailVerifyRecord
from Book_Django.settings import EMAIL_FROM
from celery import task

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


@task
def say_hello(uid,send_type='register'):
    uids = uid
    email = '130147060@qq.com'
    code = random_str(16)
    email_record = EmailVerifyRecord(code=code, email=email, send_type=send_type)
    email_record.save()
    email_title = ''
    email_body = ''
    email_title = '注册激活链接'
    email_body = "请点击下面的的链接激活你的账号:http://127.0.0.1:8000/register/activate?code={}&id={}".format(code, uids)
    send_mail(email_title, email_body, EMAIL_FROM, [email])
