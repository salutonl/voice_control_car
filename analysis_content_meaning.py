#coding:utf-8

import sys
sys.path.append("..")
from spider.weather import get_weather_info
import car_basic_config.car as car

def text_process(stt_text):
    if '向前' in stt_text or '前进' in stt_text:
        car.forward()
        return '好的，向前行驶'
    
    if '停止' in stt_text or '停' in stt_text:
        car.stop()
        return '好的，停止运行'

    if '后退' in stt_text or '向后' in stt_text:
        car.backward()
        return '好的，向后行驶'

    if '向左' in stt_text or '左转' in stt_text:
        car.TurnLeft()
        return '好的，左转弯'

    if '向右' in stt_text or '右转' in stt_text:
        car.TurnRight()
        return '好的，右转弯'

    if '天气' in stt_text or '气温' in stt_text or '温度' in stt_text:
        weather_content = get_weather_info(stt_text)
        return weather_content
    return '不好意思，小宗还不懂这个'

