# 날씨를 네이버에 검색하고 파싱하는 모듈
from flask import Flask, render_template, jsonify, make_response
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import ssl,re, json
from modules import shortURL, writejson

def weather_naver(loc):    
    try:
        context = ssl._create_unverified_context()
        enc_location = urllib.parse.quote(loc + '+날씨')
        result = urlopen('https://search.naver.com/search.naver?ie=utf8&query='+ enc_location,context=context)
        bsObj = BeautifulSoup(result.read(),"html.parser")
        whr1 = bsObj.find("span",attrs={"class":"todaytemp"}).text    #온도 가져옴
        whr2 = bsObj.find("p",attrs={"class":"cast_txt"}).text    #날씨 가져옴
        print('weather success')
        return '현재 '+loc+' '+whr1+'˚C '+whr2
    except:
        print('weather failed')
        return '날씨 정보를 가져오는데 실패했습니다!'
