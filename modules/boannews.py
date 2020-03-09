# 보안뉴스 RSS 최신뉴스 크롤링해서 json에 저장하는 모듈

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import json
import feedparser
from modules import shortURL,writejson

def boannews_update():    
    try:
        d= feedparser.parse('http://www.boannews.com/media/news_rss.xml')
        datas = dict()
        cnt = 1
        for e in d.entries:
            datas[cnt] = dict()
            datas[cnt]["title"]=e.title
            datas[cnt]["link"]=shortURL.srtURLfunc(e.link)
            writejson.writejson('./templates/get-boannews.json',datas)
            cnt=cnt+1
        print('boannews update Successed')    
    except:
        print('boannews update Failed')
        
