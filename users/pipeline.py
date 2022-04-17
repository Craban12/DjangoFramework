from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse, urlencode

import requests
from django.utils import timezone

from users.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    # api_url = urlunparse(('http', 'api.vk.com', 'method/users.get', None,
    #                       urlencode(OrderedDict(fields=','.join(('sex', 'about', 'bdate')),
    #                       access_token=response['access_token'], v=5.131)), None))
    fields = ','.join(('sex', 'about', 'bdate', 'city', 'mobile_phone', 'home_phone'))
    access_token = response['access_token']
    version = '5.131'
    api_url = f'http://api.vk.com/method/users.get?fields={fields}&access_token={access_token}&v={version}'

# _____________________________В этом участке ошибка не получается обратиться к БД, а точнее к user.userprofile.gender
    resp = requests.get(api_url)

    if resp.status_code != 200:
        return
    data = resp.json()['response'][0]
    if data['sex'] == 1:
        user.userprofile.gender = UserProfile.FEMALE
    elif data['sex'] == 2:
        user.userprofile.gender = UserProfile.MALE
    else:
        pass
    if data['about']:
        user.userprofile.about = data['about']
    bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
    age = timezone.now().date().year - bdate.year
    user.age = age
    user.save()
