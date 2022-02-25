import requests
from bs4 import BeautifulSoup
# from merge import merge_list

def extraction_rmt(url):# 리모트항목의 모든 링크에 들어가 정보를 2차원리스트로 저장
  result=requests.get(url)
  soup=BeautifulSoup(result.text,'html.parser')
  print(soup.find('body'))
  jobs=soup.find_all('tr',{'class':'job job-'})
  datas=list()  
  for job in jobs: # 각각 직업들을 불러옴
    data=list()
    data.append('remoteok')
    data.append(soup.find('a').text)
    data.append(soup.find('div',{'class':'location tooltip'}).text)
    data.append('https://remoteok.com'+soup.find('a').get('href'))
    datas.apend(data)
  #print(jobs)
  return datas