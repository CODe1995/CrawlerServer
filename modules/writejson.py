import json

#파라미터 : 경로, json Object
#기능 : 경로에 있는 json 파일에 파라미터를 써줌
def writejson(route,group):
    with open(route,'w',encoding='utf-8') as make_file:
        json.dump(group,make_file,indent='\t',ensure_ascii=False)