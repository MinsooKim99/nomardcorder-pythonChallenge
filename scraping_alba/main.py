#path is /home/runner/pythonchallengedayfive
#import requests
#from bs4 import BeautifulSoup
#import os
#import glob
#import csv
from getinfo import get_links,extract_infos
from save_csv import save_infos
    
data=extract_infos(get_links())
save_infos(data)
