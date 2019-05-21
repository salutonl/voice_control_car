#coding:utf-8
import pyaudio
import wave
import json
import sys
import os
from aip.speech import AipSpeech


from urllib2 import Request, urlopen, URLError, HTTPError


APP_ID = '16208408'
API_KEY = 'cdvXslnk2Od0uyvobCplECGN'
SECRET_KEY = 'LlSoO8pOvRjzicQYmVvo1yNiFuCSF32I'

def text_to_speech(content):
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = client.synthesis(content, 'zh', 1, {
        'vol': 5,
    })

    if not isinstance(result, dict):
        with open('synthesis.wav', 'wb') as f:
            f.write(result)
