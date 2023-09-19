from flask import Flask, jsonify, request

import sys
sys.path.append(r'c:\users\lukelim\anaconda3\envs\dev-flask\lib\site-packages')
from requests import get
import json


app = Flask(__name__)

weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric&lang=kr'
busstop_api_url = 'https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?coords={입력_좌표}&orders={변환_작업_이름}&output={출력_형식}'

# api key 가져오기
with open('api_keys.txt', 'r') as f:
    keys = f.readlines()
    WEATHER_API_KEY = keys[0]
    # BUSSTOP_API_KEY = keys[1]

## 날씨 정보 api 접속
def weather(lat, lon, appid):
    res = get(weather_api_url.format(lat, lon, appid)).text
    res = json.loads(res)
    
    weather = {
        'name' : res['name'],
        'weather' : res['weather'],
        'main' : res['main'],
        'wind' : res['wind'],
        'clouds' : res['clouds'],
        'sys' : res['sys']
    }
    return weather


## 버스정류장 정보 api 접속
def busstop(lat, lon, appid):
    return


### IN: 위도 경도
### OUT: 날씨
@app.route('/weather')
def get_weather():

    q = request.get_json()
    lat, lon = q['lat'], q['lon']

    res = weather(lat, lon, WEATHER_API_KEY)

    return jsonify(res)



### IN: 위도 경도
### OUT: 버스정류장의 도착정보
@app.route('/busstop')
def get_busstop():
    return