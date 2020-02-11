from flask import Flask, render_template, jsonify, make_response, request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import ssl
import re
import json
from modules import csnotice, boannews

app = Flask(__name__)

#JSON 파일 읽어오기


def readjson(Froute):
    try:
        with open(Froute, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(ex)
        return ''


@app.route('/')
def index():
    return render_template('index.html')

#컴공 공지사항 출력
@app.route('/get-cs')
def cs():
    response = make_response(render_template('get-cs.json'))
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return response

#보안뉴스 출력
@app.route('/get-boannews')
def boannews_print():
    response = make_response(render_template('get-boannews.json'))
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return response

#=====================================업데이트부분=============================
#인제대 학식 다인 출력
@app.route('/dain-update')
def inje_meal_dain():

    print('다인 조회')
    return render_template('index.html')

#컴공학사 공지를 가져와서 get-cs.json에 업데이트 시킨다.
#게시글 제목과 링크만
@app.route('/cs-update')
def csupdate():
    csnotice.cs_update()
    print('CS 공지사항 업데이트 완료')
    return render_template('index.html')

#보안뉴스 업데이트 함수
@app.route('/boannews-update')
def boanupdate():
    boannews.boannews_update()
    print('보안뉴스 업데이트 완료')
    return render_template('index.html')

#=====================================json처리 부분=============================
@app.route('/kakao/api/notice_cs', methods=['GET', 'POST'])
def api_notice_cs():
    dataSend = readjson('templates/get-cs.json')
    jlist = dict()
    jlist["items"] = list()
    for i in range(5):
        jlist['items'].append({
            'title': dataSend[str(i+1)]['title'],            
            'link':{
                'web':dataSend[str(i+1)]['link']
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
                        'items':jlist['items']
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

if __name__ == "__main__":
    keylist = readjson('keylist.json')
    app.run(host=keylist["ip"], port=keylist["port"])
