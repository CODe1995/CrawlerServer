from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import json
import feedparser
from modules import shortURL,writejson



def boannews_update():    
    print('boannews 업데이트') 
    d= feedparser.parse('http://www.boannews.com/media/news_rss.xml')
    datas = dict()
    cnt = 1
    for e in d.entries:
        datas[cnt] = dict()
        datas[cnt]["title"]=e.title
        datas[cnt]["link"]=shortURL.srtURLfunc(e.link)
        writejson.writejson('./templates/get-boannews.json',datas)
        cnt=cnt+1
        
