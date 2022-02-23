import requests
from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

URL="http://www.alba.co.kr/"

# 자바스크립트의 동적요소도 불러오기 위함
# 참고 https://replit.com/talk/learn/Python-Selenium-Tutorial-The-Basics/148030
# 이거 웨않뒈요??
# 해당 알바 페이지 내부에서 페이징요소랑 상호명을 따오고 싶었으나 자바스크립트 동적 요소에
# 숨겨져있어서 selenium패키지를 쓰려고 했으나 무슨짓을 해도 selenium사용이 안됩니다...
#chrome_options = Options()
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')

#driver = webdriver.Chrome(options=chrome_options)
#driver.get("https:/google.com")
#driver.get(URL)
#selenium never start...

result=requests.get(URL)
soup=BeautifulSoup(result.text,'html.parser')
#soup=BeautifulSoup(driver.page_source)
'''
def get_names():
  #name=soup.find(id='MainSuperBrand').find('ul',{'class':'goodsBox'}).find_all('a',{'class':'goodsBox-info'})
  names=list()
  companys=soup.find(id='MainSuperBrand').find('ul',{'class':'goodsBox'}).find_all('strong')
  #print(companys)
  for company in companys:
    #print(company)
    names.append(company.text.replace("/","_"))
    #print(company.text)
  #print(len(names))
  return names'''


def get_links():
  results_links=soup.find(id='MainSuperBrand').find_all('a','brandHover')
  # first_links=soup.find(id='MainSuperBrand').find_all('a','brandHover multi')
  # second_links=soup.find(id='MainSuperBrand').find_all('a',{'class':'brandHover multi second'})
  # if second_links is not None:
  #   for link_in_second in second_links:
  #     results_links.append(link_in_second)
  #   for link_in_first in first_links:
  #     results_links.append(link_in_first)
  # else:
  #   pass
  #print(results_links)
  links=list()
  for link in results_links:
    links.append(link.get('href'))
  #print(links)
  #print(len(links))
  return links
#links=get_links()

def extract_infos(links):
  count=0
  results=list()
  for link in links:
    print(f"{count+1} thing now scrapping...")
    result=requests.get(f"{link}")
    #driver.get(link)
    soup=BeautifulSoup(result.text,'html.parser')
    #soup=BeautifulSoup(driver.page_source)
    #print(soup.find(id='NormalInfo'))

    name=soup.title.text
    #names=soup.find(id='MainSuperBrand').find('ul',{'class':'goodsBox'}).find_all('strong')
    #print(name)
    if name == " 채용정보 - 알바천국":
      name=name.replace(" 채용정보 - 알바천국","donthavetitle")
      #print(name)
    else:
      name=name.replace(" 채용정보 - 알바천국","")
    #print(name)
    members_before=soup.find('tbody').find_all('tr')
    #print(members_before)
    members=list()
    for member in members_before:
      #print(member)
      if member.get('class')==['summaryView'] or member.get('class') == None:
        pass
      else:
        #print(member)
        members.append(member)
      #print(members)
    mems=list()
    if members is None:
      if name == 'donthavetitle':
        name=link-'.alba.co.kr/job/brand/'
      mems.append(name)
      mems.append("일자리 없음")
      print("저런 일자리가 없네요!")
      results.append(mems)
    for mem in members:
      #print(mem)
      # print(mem.find('td',{'class':'local first'}))
      # if mem.find('td',{'class':'local first'}) is None:
      #   mems.append(name)
      #   mems.append("일자리 없음")
      #   print("저런 일자리가 없네요!")
      # else:
      if name == 'donthavetitle':
        mems.append(mem.find('td',{'class':'title'}).find('span',{'class':'company'}).text.split()[0])
      else:
        mems.append(name)
      #print(mem.find('td',{'class':'local first'}).text.replace("\xa0"," "))
      mems.append(mem.find('td',{'class':'local first'}).text.replace("\xa0"," "))
      mems.append(mem.find('td',{'class':'title'}).find('span',{'class':'company'}).text)
      mems.append(mem.find('td',{'class':'data'}).text)
      mems.append(mem.find('td',{'class':'pay'}).text)
      mems.append(mem.find('td',{'class':'regDate last'}).text)
      #print(mems)
      #print(len(mems))
      results.append(mems)
      mems=list()
    #print(results[count])
    count+=1
  #print(results)
  #print(len(results))
  return results