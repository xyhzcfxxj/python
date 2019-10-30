from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '17522858'
API_KEY = "DRDzSY7HEcGXG3KKccb05sIA"
SECRET_KEY = "mounL0borhSLGVjMqFoYdxCUlETyo5zQ"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

AUDIO_FILE = './audio/16k.pcm'
DEV_PID = 1536
FORMAT = AUDIO_FILE[-3:]


def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()


response = client.asr(get_file_content(AUDIO_FILE), 'pcm', 16000, {
    'dev_pid': 1536,
})

print(response)
