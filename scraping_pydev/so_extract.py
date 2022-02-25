import requests
from bs4 import BeautifulSoup
from merge import merge_list

def extraction_so(url):# 제목 회사명 링크 등 최종결과들을 2차원리스트로 반환
  result=requests.get(url)
  soup=BeautifulSoup(result.text,'html.parser')
  pages=soup.find('div',{'class':'s-pagination'}).find_all('a',{'class':'s-pagination--item'})
  links_page=list()
  for page in pages: # 검색결과의 각 페이지의 링크들을 모음
    links_page.append(page.get('href'))
  links_page=links_page[:-1]
  #print(links_page)
  links=list()
  jobs=list()
  companies=list()  
  for link_page in links_page:# 페이지당 하나하나씩
    page_result=requests.get(f'https://stackoverflow.com{link_page}')
    soup_page=BeautifulSoup(page_result.text,'html.parser')
    link_before=soup_page.find_all('a',{'class':'s-link stretched-link'})
    for link in link_before: # 링크를 따옴
      links.append('https://stackoverflow.com'+link.get('href'))
      jobs.append(link.text)
    links_companies=soup_page.find_all('h3',{'class':'fc-black-700 fs-body1 mb4'})
    #links_companies=soup_page.find('h3',{'class':'fc-black-700 fs-body1 mb4'}).find_all('span')
    #print(links_companies)
    for company in links_companies: # 회사명과 지역을 따옴
      #print(company.text)
      company_text=company.text.replace('  ','').replace('•',' ').replace('\r','').replace('\n','')
      companies.append(company_text)
  #print(links)
  #print(len(links))
  #print(jobs)
  #print(len(jobs))
  #print(companies)
  #print(len(companies))
  where=['stackoverflow' for x in range(len(jobs))]
  datas=merge_list(where,jobs,companies,links)
  #print(datas)
  return datas # datas = [[제목1,주소및회사1,링크1],[제목2,주소및회사2,링크2], ...]