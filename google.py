from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


driver = webdriver.Chrome() #웹 드라이버로 크롬을 사용
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl") #사용할 웹페이지
elem = driver.find_element_by_name("q")
elem.send_keys("미소") #검색할 키워드
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

#Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight") #자바 스크립트 코드로 브라우저 높이를 찾아 저장

while True:
    #Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #브라우저 끝까지 스크롤을 내린다.

    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME) #쉬는시간

    #Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight") #브라우저 높이를 다시 구함
    if new_height == last_height: # 만약 새로찾은 높이랑 기존 높이랑 같다면 스크롤을 모두 내려 찾을게 없다는것이다.
        try: #만약 아래 조건에서 오류가 났을떄
            driver.find_element_by_css_selector(".mye4qd").click() #(결과 더보기 버튼을 클릭해라)
        except: #반복문을 탈출하라
            break

    last_height = new_height# 새로 찾은 높이를 기존 높이에 저장


images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") #작은 이미지
count = 1
for image in images: #작은 이미지를 뽑는다.

    try:
        image.click() #class에 맞는걸 찾아서 클릭하게 만다. (css를 알아야 이해 가능) // 클릭하면 큰 사진이 나오게 된다.
        time.sleep(3) #이미지가 다 로딩되지 않고 다운하거나 출력하는걸 방지하기 위해 3초정도 쉬게 만든다.
        imgurl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src") #큰이미지의 url을 찾고
        urllib.request.urlretrieve(imgurl, str(count) + ".jpg") #이미지를 다운한다.
        count += 1
    except: #오류가 난다면 그냥 패스해라
        pass

driver.close() # 모든 이미지가 다운되면 드라이버(브라우저 창) 을 닫는다.

#이미지가 아니더라도 write를 사용해 단어들을 받아올수도 있으며 내가 원하는 사진들을 키워드를 바꾸고 각 class에 맞춰서 다운할수 있도록 해주면 자동화 할수 있다.