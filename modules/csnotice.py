# 인제대컴공 공지사항 크롤링해서 json에 업데이트하는 모듈
from flask import Flask, render_template, jsonify, make_response
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import ssl,re, json
from modules import shortURL, writejson

def cs_update():    
    print('cs 업데이트') 
    context = ssl._create_unverified_context()
    result = urlopen('https://cs.inje.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad-2/',context=context)
    bsObj = BeautifulSoup(result.read(),"html.parser")
    cstxt = bsObj.find_all("td",attrs={"class":"kboard-list-title"})    #공지사항란만 가져옴
    links =[]#게시물 URL이 담김
    titles=[]#게시물 제목이 담김
    results=dict()#JSON 형식으로 저장될 공간
    pattern = re.compile(r'\t+')#두칸짜리 공백 정규식
    pattern2 = re.compile(r'\n')#"\n"
    cnt = 1
    for i in range(0,len(cstxt)):
        for link in cstxt[i].find_all('a'):
            links.append(shortURL.srtURLfunc(urllib.parse.unquote("https://cs.inje.ac.kr"+link.get('href'))))
            titles.append(link.find("div",attrs={"class":"kboard-default-cut-strings"}).text)        
    for i in range(0,len(links)):
        results[cnt]=dict()
        results[cnt]["title"]=re.sub(pattern2,'',re.sub(pattern,'',titles[i]))
        results[cnt]["link"]=links[i]
        cnt = cnt+1
    writejson.writejson('./templates/get-cs.json',results)    