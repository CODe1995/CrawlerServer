# acmicpc 인제대 랭크순위
from flask import Flask, render_template, jsonify, make_response
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import ssl,re, json
from modules import writejson

def acmicpc_rank():    
    try:
        # context = ssl._create_unverified_context()
        result = urlopen('https://www.acmicpc.net/school/ranklist/353')
        bsObj = BeautifulSoup(result.read(),"html.parser")
        ranklist = bsObj.find("table",{'id':'ranklist'})
        rankarr = ranklist.find_all('a')
        rankj = dict()
        print('acmicpc rank success')
        num = 1
        for i,txt in enumerate(rankarr):
            tmp = i+1
            if tmp%3==1:
                rankj[num] = dict()
                rankj[num]["rank"]=num
                rankj[num]["id"] = txt.text
            elif tmp%3==2:
                rankj[num]["맞은문제"] = txt.text
            else:
                rankj[num]["제출"] = txt.text
                num+=1   
        writejson.writejson('./templates/acmicpcrank.json',rankj)
        return 'done'
    except:
        print('acmicpc rank failed')
        return 'acmicpc rank failed'
