# 카카오 오픈빌더에 JSON 형태로 보내는 함수를 정리해 놓음.
# app.py에 나열하면 복잡해지기 때문에,,
from flask import jsonify
import json
def readjson(Froute):
    try:
        with open(Froute, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(ex)
        return ''

def api_dain():
    return

def api_break():            #휴학
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "휴학은 여기서 해결할 수 있어!",
                            "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                        },
                        "items": [
                            {
                                "title": "휴학에 대해 알아보기",
                                "description": "휴학종류와 기간에 대해 알려줄게!",
                                "imageUrl": "",
                                "link": {
                                    "web": key['break'][0]
                                }
                            },
                            {
                                "title": "휴학 절차에 대해 알아보기",
                                "description": "휴학 방법과 절차에 대해 알려줄게!",
                                "imageUrl": "",
                                "link": {
                                    "web": key['break'][1]
                                }
                            },
                            {
                                "title": "군휴학/일반휴학 전환",
                                "description": "군휴학과 일반휴학 절차는 조금씩 달라!",
                                "imageUrl": "",
                                "link": {
                                    "web": key['break'][2]
                                }
                            },
                            {
                                "title": "휴학에 따른 등록금 대체",
                                "description": "휴학에따라 등록금 처리 안내",
                                "imageUrl": "",
                                "link": {
                                    "web": key['break'][3]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(data)

def api_back():             #복학
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "복학은 여기서 해결할 수 있어!",
                            "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                        },
                        "items": [
                            {
                                "title": "복학에 대해 알아보기",
                                "description": "복학종류와 기간에 대해 알려줄게!",
                                "imageUrl": "",
                                "link": {
                                    "web": key['back'][0]
                                }
                            },
                            {
                                "title": "복학 절차에 대해 알아보기",
                                "description": "복학 방법과 절차에 대해 알려줄게!",
                                "imageUrl": "",
                                "link": {
                                    "web": key['back'][1]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(data)

def api_subjectapply():     #수강신청
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "수강신청이 궁금해?",
                            "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                        },
                        "items": [
                            {
                                "title": "수강신청에 대해 알아보기",
                                "description": "수강신청에 대해서",
                                "imageUrl": "",
                                "link": {
                                    "web": key['subjectapply'][0]
                                }
                            },
                            {
                                "title": "수강신청 방법에 대해 알아보기",
                                "description": "방법과 절차에 대해 알려줄게!",
                                "imageUrl": "",
                                "link": {
                                    "web": key['subjectapply'][1]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(data)

def api_tuitionpayment():   #등록금 납부
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "등록금 납부에 대한 정보야!",
                            "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                        },
                        "items": [
                            {
                                "title": "등록금 납입에 대한 설명",
                                "description": "납입기간과 장소 등에 대한 설명이야!",
                                "imageUrl": "",
                                "link": {
                                    "web": key['tuitionpayment'][0]
                                }
                            },
                            {
                                "title": "등록금 납입 방법 알아보기",
                                "description": "등록금 납부액 확인방법과 절차야!",
                                "imageUrl": "",
                                "link": {
                                    "web": key['tuitionpayment'][1]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(data)

def api_graduation():       #졸업
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "졸업 대한 정보야!",
                            "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                        },
                        "items": [
                            {
                                "title": "컴퓨터공학부 졸업정보",
                                "description": "졸업학점과 조회방법에 대해서",
                                "imageUrl": "",
                                "link": {
                                    "web": key['graduation'][0]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(data)

def api_volunteer():        #봉사활동
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "봉사활동 대한 정보야!",
                            "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                        },
                        "items": [
                            {
                                "title": "봉사활동 정보와 절차",
                                "description": "인정범위와 절차",
                                "imageUrl": "",
                                "link": {
                                    "web": key['volunteer'][0]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(data)

def api_absent():           #공인결석원
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "공인결석에 대한 정보야!",
                            "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                        },
                        "items": [
                            {
                                "title": "공인결석 인정 범위",
                                "description": "인정범위와 기간",
                                "imageUrl": "",
                                "link": {
                                    "web": key['absent'][0]
                                }
                            },
                            {
                                "title": "공결 절차와 제출기한",
                                "description": "유형에 따른 신청절차, 제출 기한",
                                "imageUrl": "",
                                "link": {
                                    "web": key['absent'][1]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(data)


key = readjson('keylist.json')
