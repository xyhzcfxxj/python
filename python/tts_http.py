import json
import requests
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen
from urllib.request import Request

APP_ID = 17522858
API_KEY = "DRDzSY7HEcGXG3KKccb05sIA"
SECRET_KEY = "mounL0borhSLGVjMqFoYdxCUlETyo5zQ"

TOKEN_URL = 'https://openapi.baidu.com/oauth/2.0/token'
TTS_URL = 'http://tsn.baidu.com/text2audio'


def get_token(apikey, secretkey, tokenurl):
    param = {"grant_type": "client_credentials", "client_id": apikey, "client_secret": secretkey}
    req = requests.get(tokenurl, param)
    print(req.text)
    response = json.loads(req.text)
    token = response['access_token']
    return token


def get_tts(token, text):
    param = {
        'tex': text,
        'tok': token,
        'cuid': 'xyhtest',
        'ctp': 1,
        'lan': 'zh',
        'per':4,
        'spd':5,
        'pit':5,
        'vol':5,
        'aue':3
    }
    param_json = urlencode(param)
    response = requests.post(TTS_URL, data=param_json.encode('utf-8'))
    print(param_json)
    result=response.content
    print(result)

    # data = urlencode(param)
    # req = Request(TTS_URL, data.encode('utf-8'))
    # f = urlopen(req)
    # result_str = f.read()
    # print('-----')
    # print(result_str)

    save_file = 'result.mp3'
    with open(save_file, 'wb') as of:
        of.write(bytes(response.text,encoding='utf-8'))


if __name__ == '__main__':
    token = get_token(API_KEY, SECRET_KEY, TOKEN_URL)
    text = '北京欢迎你'
    tex = quote_plus(text)
    get_tts(token, tex)
    print(tex)
