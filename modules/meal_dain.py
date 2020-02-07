from flask import Flask, render_template, jsonify, make_response
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import ssl,re, json
import writejson


def dain_update():    
    context = ssl._create_unverified_context()
    result = urlopen('https://www.inje.ac.kr/kor/Template/Bsub_page.asp?Ltype=5&Ltype2=3&Ltype3=3&Tname=S_Food&Ldir=board/S_Food&Lpage=s_food_view&d1n=5&d2n=4&d3n=4&d4n=0',context=context)
    bsObj = BeautifulSoup(result.read(),"html.parser")
    txta = bsObj.find_all("td",attrs={"class":"tc"})
    result = dict()
    daylist = ['월','화','수','목','금']
    for i in range(0,4):        
        result[daylist[i]] = dict()

    for i in range(0,len(txta)):        
        # print("[",i+1,"]",txta[i].get_text())
        print(txta[i].string)
    
    #txt = str(bsObj) 

dain_update()