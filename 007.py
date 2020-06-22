import requests, re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')


#BeautifulSoup의 find_all() 명령에 찾고자 하는 태그 이름을 매개변수로 전달하면, 웹 문서에서 해당하는 모든 태그를 찾아서 리스트 형태로 리턴한다.
#따라서 soup 객체에 들어있는 모든 <a> 태그를 찾고 변수 links 에 저장한다.
links = soup.find_all("a")
print("하아퍼링크의 개수: ", len(links))
print("\n")
print("첫 3개의 원소:", links[:3])
print("\n")

#"/wiki/" 문자열이 링크에 포함되어 있는 <a> 태그를 3개 찾아서 변수 link_links에 저장한다.
wiki_links = soup.find_all(name='a', href = re.compile("/wiki/"), limit=3)
print("/wiki/ 문자열이 포함된 하이퍼링크:", wiki_links)
print("\n")

external_links = soup.find_all(name='a', atts={"class":"external text"}, limit=3)
print("class 속성으로 추출한 하이퍼링크", external_links)

