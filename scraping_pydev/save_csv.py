import os
import csv
import glob

def save(datas):# 2차원리스트의 데이터들을 csv로 저장
  csv_link=glob.glob('/home/runner/pythonchallengedaylast/jobs_data/*.csv')
  site_from=datas[0][0] # 어느사이트인지(stackoverflow weworkremotely remoteok)
  if csv_link is None:
    with open(f'{site_from}.csv','w',newline='') as s:
        wr_s=csv.writer(s)
        wr_s.writerow(['title | name/region/others | link'])
  else:
    os.chdir('/home/runner/pythonchallengedaylast/jobs_data')
    with open(f'{site_from}.csv','w',newline='') as f:
         wr_f=csv.writer(f)
         wr_f.writerow(['title | name/region/others | link'])
    for data in datas:
      with open(f'{data[0]}.csv','a',newline='') as g:
        wr_g=csv.writer(g)
        data=data[1:]
        #print(data)
        wr_g.writerow(data)
  with open(f'{site_from}.csv','a',newline='') as h:
    wr_h=csv.writer(h)
    wr_h.writerow([f'{site_from} has {str(len(datas))} jobs!'])
  print("site complete!")