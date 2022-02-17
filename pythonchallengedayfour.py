# import os
import requests

# indeed_result=requests.get('https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50&vjk=c9206c4cf58de0d1')
# print(indeed_result.status_code)

# not_result=requests.get('https://www.asfffsad.com')
# print(not_result.status_code)

def check_url(answer_url):
  answer_url=str.lower(answer_url)
  urls=answer_url.split(',')
  # return urls
  for url in urls:
    url=url.strip()
    if "https://" not in url:
      url="https://"+url
    try:
      result=requests.get(url)
      sta=result.status_code
    except Exception:
      print(f"{url} is not a valid url.")
      continue
    if sta != 200:
      print(f"{url} is down!")
    else:
      print(f"{url} is up!")

def repeat():
  while True:
    answer=input("Do you want go up?(Y/N)")
    if answer == 'Y' or answer == 'y':
      return True
    elif answer == 'N' or answer == 'n':
      return False
    else:
      print("not correct answer!")

print("It is URL check program.")
while True:
  your_answer=input("Please write a URL or URLs you want  to check. (separated by comma)\n")
  check_url(your_answer)
  you_want_continue=repeat()
  if you_want_continue:
    # os.system('cls') #Error in repl only: I think os package is not avilable in repl
    print("\x1B[H\x1B[J")
    continue
  else:
    print("OK. Bye~")
    break