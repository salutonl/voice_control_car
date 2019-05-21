
# -*-coding: UTF-8 -*-
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

def parse():
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


    text = client.asr(get_file_content('output.wav'), 'wav', 16000, {
        'dev_pid': 1537,
    })
    print text
    try:
        results = text["result"]
    except:
        results = False
    voice_parse = "".join(results)
    return results