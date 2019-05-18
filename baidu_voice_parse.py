#coding:utf-8
import pyaudio
import wave
from baidu_speech_api import BaiduVoiceApi
import json
import signal
import sys
import RPi.GPIO as GPIO
import os
from aip.speech import AipSpeech

from urllib2 import Request, urlopen, URLError, HTTPError


RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 1
RESPEAKER_WIDTH = 2
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

APP_ID = '16208408'
API_KEY = 'cdvXslnk2Od0uyvobCplECGN'
SECRET_KEY = 'LlSoO8pOvRjzicQYmVvo1yNiFuCSF32I'

baidu = BaiduVoiceApi(appkey=API_KEY,secretkey=SECRET_KEY)


def record():
    p = pyaudio.PyAudio()
    stream = p.open(
            rate=RESPEAKER_RATE,
            format=p.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            input=True,
            start=False,)
    stream.start_stream()
    print("* recording")
    frames = []
    for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(RESPEAKER_CHANNELS)
    wf.setsampwidth(p.get_format_from_width(RESPEAKER_WIDTH))
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b'',join(frames))
    wf.close()