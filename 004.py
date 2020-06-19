import requests
from bs4 import BeautifulSoup
#roboturl = "https://en.wikipedia.org/robots.txt"
#resp = requests.get(roboturl)
#print(resp.text)

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
url2= "https://www.tta.or.kr/"
resp = requests.get(url2)
html_src =resp.text


soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print("\n")

print(soup.head)
print("\n")

print(soup.body)
print("\n")

print('title 태그 요소:', soup.title)
print('title 태그 이름:', soup.title.name)
print('title 태그 문자열:', soup.title.string)
