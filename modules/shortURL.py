#NAVER SHORT API를 이용해서 단축 URL 만들기
import os
import sys
import urllib.request
import json

#targetURL에 단축시키고픈 URL을 넣으면 단축된 URL을 리턴시킴
def srtURLfunc(targetUrl):
    with open('naverData.json') as json_file:
        json_data = json.load(json_file)
        CLIENT_ID = json_data["id"] # 개발자센터에서 발급받은 Client ID 값
        
        CLIENT_SECRET = json_data["secret"] # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(targetUrl)
        data = "url=" + encText
        url = "https://openapi.naver.com/v1/util/shorturl"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",CLIENT_ID)
        request.add_header("X-Naver-Client-Secret",CLIENT_SECRET)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = json.load(response)#json 형태로 return 되기 때문에 json.load 사용
            return(response_body["result"]["url"])#result -> url 태그에 있으므로 단축된 url만 가져옴
        else:
            return("Error Code:"+rescode)