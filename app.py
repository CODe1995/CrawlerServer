from flask import Flask, render_template, jsonify, make_response, request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import ssl
import re
import json
from modules import csnotice, boannews, Scapture, apicontrol
import os
#쓰레드
import time
import threading
app = Flask(__name__)

def thread_run():
    print('=====',time.ctime(),'=====')
    csnotice.cs_update()    #학사 공지 업데이트
    boannews.boannews_update()    #보안뉴스 최신 업데이트
    link = 'https://www.inje.ac.kr/kor/Template/Bsub_page.asp?Ltype=5&Ltype2=3&Ltype3=3&Tname=S_Food&Ldir=board/S_Food&Lpage=s_food_view&d1n=5&d2n=4&d3n=4&d4n=0'
    Scapture.func_capture(link, 'id', 'table1', 0, os.getcwd()+'/static/images/다인메뉴.png')    #학식 업데이트
    threading.Timer(3600,thread_run).start()

# def update_set():
#     inje_meal_dain()
#     csupdate()
#     boanupdate()

#JSON 파일 읽어오기
def readjson(Froute):
    try:
        with open(Froute, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(ex)
        return ''

# @app.route('/')
# def index():
#     return render_template('index.html')

#=====================================API 반환 부분=============================
# @app.route('/kakao/api/weather',methods=['GET','POST'])
# def api_weather():
#     return apicontrol.api_weather(loc)

@app.route('/kakao/api/notice_cs', methods=['GET', 'POST'])
def api_notice_cs():
    dataSend = readjson('templates/get-cs.json')
    jlist = dict()
    jlist["items"] = list()
    for i in range(5):
        jlist['items'].append({
            'title': dataSend[str(i+1)]['title'],
            'link': {
                'web': dataSend[str(i+1)]['link']
            }
        })
    manuData = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "컴퓨터공학부 공지사항",
                            "imageUrl": "https://cs.inje.ac.kr/wp-content/uploads/2019/07/가로1_한영_컬러_저용량.jpg"
                        },
                        'items': jlist['items']
                    }
                }
            ]
        }
    }
    # print(json.dumps(manuData,indent='\t'))
    return jsonify(manuData)

@app.route('/kakao/api/boannews', methods=['GET', 'POST'])
def api_boannews():
    dataSend = readjson('templates/get-boannews.json')
    return jsonify(dataSend)

@app.route('/kakao/api/dain', methods=['GET', 'POST'])
def kakaodain():    #다인메뉴판
    return apicontrol.api_dain()

@app.route('/kakao/api/hayeongwan', methods=['GET', 'POST'])
def kakaohayeongwan():  #하연관메뉴판 업데이트 요망!
    return '하연관메뉴.png'

@app.route('/kakao/api/break',methods=['GET','POST'])
def apibreak(): #휴학
    return apicontrol.api_break()

@app.route('/kakao/api/back',methods=['GET','POST'])
def apiback():  #복학
    return apicontrol.api_back()

@app.route('/kakao/api/subjectapply',methods=['GET','POST'])
def apisubjectapply(): #수강신청
    return apicontrol.api_subjectapply()

@app.route('/kakao/api/tuitionpayment',methods=['GET','POST'])
def apituitionpayment(): #등록금 납부/납입
    return apicontrol.api_tuitionpayment()

@app.route('/kakao/api/graduation',methods=['GET','POST'])
def apigraduation():    #졸업
    return apicontrol.api_graduation()

@app.route('/kakao/api/volunteer',methods=['GET','POST'])
def apivolunteer():    #봉사활동
    return apicontrol.api_volunteer()

@app.route('/kakao/api/absent',methods=['GET','POST'])
def apiabsent():        #공인결석원
    return apicontrol.api_absent()

#=====================================메인함수=============================
if __name__ == "__main__":
    keylist = readjson('keylist.json')    
    thread_run()
    app.run(host=keylist["ip"], port=keylist["port"])
    

