import requests
from bs4 import BeautifulSoup

def extraction_wwr(url):# 모든 링크에서 정보를 가져와 2차원리스트로 저장
  result=requests.get(url)
  soup=BeautifulSoup(result.text,'html.parser')
  kind_of_jobs=soup.find_all('li',{'class':'view-all'})
  #print(kind_of_jobs)
  link_kind_of_jobs=list()
  for link in kind_of_jobs: # Fullstack backend other 3종류의 링크를 가져옴
    link_kind_of_jobs.append('https://weworkremotely.com'+link.find('a').get('href'))
  #print(link_kind_of_jobs)

  datas=list()
  for link in link_kind_of_jobs: # Fullstack backend other 3종류의 링크에 각각 들어가 정보를 가져옴
    result_detail=requests.get(link)
    soup_detail=BeautifulSoup(result_detail.text,'html.parser')
    job_lists=soup_detail.find('section',{'class':'jobs'}).find_all('li')
    for job in job_lists: # 링크 하나하나에서 정보를 가져옴
      #print(job)
      data=list()
      if job.find('span',{'class':'title'}) is None:
        pass
      else:
        data.append('weworkremotely')
        data.append(job.find('span',{'class':'title'}).text)
        #print(job.find('span',{'class':'region company'}))
        if job.find('span',{'class':'region company'}) is None:
          data.append("region data does not exist")
        else:
          data.append(job.find('span',{'class':'region company'}).text)
        #print(job.find('a').get('href'))
        data.append('https://weworkremotely.com'+job.find('a').get('href'))
        datas.append(data)
  #print(datas)
  #print(len(datas))
  return datas # datas = [[제목1,주소및회사1,링크1],[제목2,주소및회사2,링크2], ...]