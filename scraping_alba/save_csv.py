import csv
import os
import glob

def save_infos(datas):
  csv_link=glob.glob('/home/runner/pythonchallengedayfive/alba_data/*.csv')
  for csv_file in csv_link:
    #os.remove(csv_file)
    with open(csv_file,'w',newline='',encoding='utf-8') as g:
      wr_g=csv.writer(g)
      wr_g.writerow(['place','title','time','pay','date'])
  os.chdir('/home/runner/pythonchallengedayfive/alba_data')
  for data in datas:
    with open(f'{data[0]}.csv','a',newline='',encoding='utf-8') as f:
      wr_f=csv.writer(f)
      data=data[1:]
      #print(data)
      wr_f.writerow(data)

  print("complete!")