# 라이브러리를 불러 온다.
import requests
from bs4 import BeautifulSoup

#웹 페이지 문서의 HTML 소스코드를 파싱하여 BeautifulSoup 객체를 생성한다. 변수 soup에 저장한다.
url="https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp=requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

#BeautifulSoup 의 select() 메소드는 find_all() 메소드와 비슷하다. 찾으려는 태그 이름을 매개변수로 전달하면,
#웹 문서에서해당하는 모든 태그를 찾아서 리스트 형태로 리턴한다. 

#links = soup.select('a')
links = soup.find_all("a")
print(len(links))
print("\n")

#앞에서 3개의 원소를 리스트 슬라이싱 기법으로 선택하고 출력해 본다.
print(links[:3])
print("\n")


external_links = soup.select('a[class="external text"]')
print(external_links[:3])
print("\n")

id_selector = soup.select('#siteNotice')
print(id_selector)
print("\n")

id_selector2 = soup.select('div#siteNotice')
print(id_selector2)
print("\n")

id_selector3 = soup.select('p#siteNotice')
print(id_selector3)
print("\n")

class_selector = soup.select('.mw-headline')
print(class_selector)
print("\n")

class_selector2 = soup.select('span.mw-headline')
print(class_selector2)
