import requests
import json
import base64

APPID = 17522858
API_Key = "DRDzSY7HEcGXG3KKccb05sIA"
Secret_Key = "mounL0borhSLGVjMqFoYdxCUlETyo5zQ"

TOKEN_URL = 'https://openapi.baidu.com/oauth/2.0/token'
ASR_URL = 'http://vop.baidu.com/server_api'

AUDIO_FILE = './audio/test.wav∂'
DEV_PID = 1536
FORMAT = AUDIO_FILE[-3:]  # 文件后缀只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式

CUID = '123456PYTHON'
# 采样率
RATE = 16000  # 固定值


def get_token(API_Key, Secret_Key, TOKEN_URL):
    param = {"grant_type": "client_credentials", "client_id": API_Key, "client_secret": Secret_Key}
    req = requests.get(TOKEN_URL, param)
    print(req.text)
    response = json.loads(req.text)
    token = response['access_token']
    return token


def get_asr(token):
    with open(AUDIO_FILE, 'rb', ) as audio_file:
        speech_data = audio_file.read()
    speech_base64 = base64.b64encode(speech_data)
    length = len(speech_data)
    speech = str(speech_base64, 'utf-8')
    param = {'dev_pid': DEV_PID,
             # "lm_id" : LM_ID,    #测试自训练平台开启此项
             'format': FORMAT,
             'rate': RATE,
             'token': token,
             'cuid': CUID,
             'channel': 1,
             'speech': speech,
             'len': length
             }
    test=1
    param_json = json.dumps(param)
    print(param_json)
    header = {'Content-Type': 'application/json'}
    response = requests.post(ASR_URL, headers=header, data=param_json)
    print(response.text)
    result = json.loads(response.text)['result']
    return result[0]


if __name__ == "__main__":
    token = get_token(API_Key, Secret_Key, TOKEN_URL)
    result = get_asr(token)

    print(result)