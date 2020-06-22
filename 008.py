import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp=requests.get(url)
html_src=resp.text
soup=BeautifulSoup(html_src, 'html.parser')

# 크롬 개발자 도구에서  Copy 한 CSS 선택자를  selelt() 메소드에 전달한다. select() 메소드가 리턴하는 객체를 변수 subway_image에 저장한다
# select()메소드가 리턴하는 객체는 파이썬 리스트이다. subway_image 변수를 print() 함수를 사용하여 출력해보면 원소 1개 (<img> 태그)를 갖는다. 이 웹페이지에는 select() 메소드에 
# 전달한 CSS 선택자가 가리키는 태그가 1개반 존재한다는 것을 알 수 있다.
subway_imege = soup.select("#mw-content-text > div > table:nth-child(3) > tbody > tr:nth-child(2) > td > a > img")
print(subway_imege)
print("\n")
print(subway_imege[0])
print("\n")

subway_imege2=soup.select('tr>td>a>img')
print(subway_imege2[1])
