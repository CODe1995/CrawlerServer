from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from PIL import Image
from io import BytesIO

#url : 해당 페이지 url
#choice : class인지 id인지 선택 'class', 'id'
#target : 해당 elementid 또는 classname 검색
#level : 중복되는 경우 몇번째 요소인지 default=0
#fname : png로 저장될 이름
def func_capture(url,choice,target,level,fname):
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--start-maximized')
        options.headless = True
        driver = webdriver.Chrome(options=options) 
        driver.get(url)      
        # 전체 페이지의 사이즈를 구하여 브라우저의 창 크기를 확대하고 스크린캡처를 합니다.    
        page_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        page_height = driver.execute_script('return document.body.parentNode.scrollHeight')    
        driver.set_window_size(page_width, page_height)
        png = driver.get_screenshot_as_png()
        
        # 특정 element의 위치를 구하고 selenium 창을 닫습니다.
        if choice=='id':
            element = driver.find_elements_by_id(target)[level]
        elif choice=='class':
            element = driver.find_elements_by_name(target)[level]
        image_location = element.location
        image_size = element.size
        driver.quit()
        
        # 이미지를 element의 위치에 맞춰서 crop 하고 저장합니다.
        im = Image.open(BytesIO(png))
        left = image_location['x']
        top = image_location['y']
        right = image_location['x'] + image_size['width']
        bottom = image_location['y'] + image_size['height']
        im = im.crop((left, top, right, bottom))
        im.save(fname)
        print('capture Successed!')
    except:
        print('capture Failed!')

