# 1일차 퀴즈 관련
import time

myNameIs = "nico"
print(myNameIs)

my_name_is = "nico"
print(my_name_is)

dic = {"tup":("T","U","P","L","E")}
print(dic)
print(dic["tup"])


######################################################################################################################
# 2일차 퀴즈 관련

# This Blueprint code is broken. There are some functions missing, you need to create them. When you run the code, the output must look like this!
#오늘의 과제를 열어보시면 제대로 작동하지 않습니다. 그 이유는 프로그램이 돌아가기 위한 몇몇 코드들이 없기 때문입니다. 그러므로 프로그램이 제대로 돌아가기 위해 여러분들이 직접 코드를 작성 하셔야 됩니다.

"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

# 입력된 문자열이 리스트에 있는지 확인
def is_on_list(list, string):
  if string in list:
    return "True"
  return "False"

# 리스트의 n 번째 요소 출력
def get_x(list, integer):
  return list[integer]

# 리스트에 요소 추가
def add_x(list, string):
  list.append(string)
  return list

# 리스트에서 요소 삭제
def remove_x(list, string):
  list.remove(string)
  return list

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #


######################################################################################################################
# 3 일차
# 답안: https://gist.github.com/serranoarevalo/a830deafa1dc133b8f4e6ee19e56d0be

dictionary = {}
dictionary["a"] = "A"
print(dictionary)

"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""

def add_to_dict(dic,*args):
  if type(dic) != dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif len(args) != 2:
    print("You need to send a word and a definition.")
  elif args[0] in dic:
    print(f"{args[0]} is already on dictionary. Won't add.")
  else:
    print(f"{args[0]} has benn added.")
    dic[args[0]] = args[1]
  pass

def get_from_dict(dic,*args):
  if type(dic) != dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif len(args) != 1:
    print("You need to send a word to search for.")
  elif args[0] in dic:
    print(f"{args[0]}: {dic[args[0]]}")
  else:
    print(f"{args[0]} was not found in this dict.")
  pass

def update_word(dic,*args):
  if type(dic) != dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif len(args) != 2:
    print("You need to send a word and a definition to update.")
  elif args[0] in dic:
    print(f"{args[0]} has been updated to: {dic[args[0]]}")
  else:
    print(f"{args[0]} is no on the dict. Can't update non-existing word.")
  pass

def delete_from_dict(dic,*args):
  if type(dic) != dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif len(args) != 1:
    print("You need to specify a word to delete.")
  elif args[0] in dic:
    print(f"{args[0]} has been deleted.")
    dic.pop(args[0])
  else:
    print(f"{args[0]} is not in tihs dict. Won't delete.")
  pass

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\


######################################################################################################################
# 4일차
# 답안: https://gist.github.com/serranoarevalo/8608a7e39af7f634f11184756c2463f5

import os
import requests

# Using the boilerplate, make a program that gets urls as an input and checks if they are online or not.
# 보일러플레이트를 이용해 URL을 입력받아 온라인 상태인지 아닌지 체크하는 프로그램을 만드세요.
# 프로그램은 쉼표로 URL의 개수를 구별합니다. 또한 ‘http’의 유무와 공백을 체크하여 ‘http’가 없다면 추가해주고 공백은 모두 제거해 줍니다. 대문자가 포함되어 있을 경우도 생각하여 소문자로 변환시켜줍니다. 이러한 경우들을 모두 생각하여 처리해줍시다.
# URL이 실제로 존재하는지 존재하지 않는지 체크해야 됩니다.
# 사용자들은 프로그램이 모두 종료된 후 다시 시작할 수 있습니다.

def redo(string):
  if string == "y":
    os.system("clear")
    return 1
  elif string == "n":
    return 2
  else:
    print("That's not a valid answer")
    return redo(input("Do you want to start over? y/n"))

def make_urls(list):
  list_rev=[]
  for i in list:
    i=i.replace(" ","").lower()
    # i=i.strip().lower()
    if "http://" not in i:
      i="http://"+i
    list_rev.append(i)
  return list_rev

while True:
  print(f"""Welcome to IsItDown.py!
Please write a URL or URLs you want to check. (separated by comma)""")
  urls=list(map(str,input().split(",")))
  urls=make_urls(urls)
  for i in urls:
    try:
      req = requests.get(i)
      """1xx - informational
      2xx - success
      3xx - redirection
      4xx - client error
      5xx - server error"""
      if 200<=req.status_code<300:
        print(f"{i} is up!")
    except:
      if ".com" not in i and "co.kr" not in i:
        print(f"{i} is not a valid URL.")
      else:
        print(f"{i} is down!")
  call = redo(input("Do you want to start over? y/n"))
  if call == 1:
    continue
  else:
    break
print("k. bye!")


######################################################################################################################
# 5일차
# 답안: https://replit.com/@kariray/Day8#main.py

import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

# goodbox에서 각 브랜드 링크 확인
get_url = requests.get(alba_url)
soup = BeautifulSoup(get_url.text, "html.parser")
get_goodsbox = soup.find_all("li", {"class": "impact"})

for i in get_goodsbox:
  company = i.find("span", {"class": "company"}).text
  href = i.find("a")["href"]

  # 받아온 브랜드 링크(href)에서 알바 정보 확인
  h_get_url = requests.get(href)
  h_soup = BeautifulSoup(h_get_url.text, "html.parser")

  # goodslist에서 알바 정보 확인
  get_goodslist = h_soup.find_all("tr",{"class": "divide"})
  alba_dict={}
  alba_list=[]
  for i in get_goodslist:
    # i.find("td", {"class": "local first"}.text = 알바 지역
    place = i.find("td", {"class": "local first"}).text
    # i.find("td", {"class": "company"}.text = 알바 회사명
    title = i.find("span", {"class": "company"}).text
    # i.find("td", {"class": "data"}).text = 알바 시간
    time = i.find("td", {"class": "data"}).text
    # i.find("td", {"class": "pay"}).text = 급여
    pay = i.find("td", {"class": "pay"}).text
    # i.find("td", {"class": "regDate last"}).text = 등록일
    date = i.find("td", {"class": "regDate last"}).text
    alba_dict = {
      "place": place.replace("\xa0"," "), # 이상한 문자열 삭제
      "title": title,
      "time": time,
      "pay": pay,
      "date": date
    }
    alba_list.append(alba_dict)

  file = open(f"{company.replace('/','_')}.csv", "w") # 회사 이름에 / 가 있으면 파일 이름으로 넣을 수 없음
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])
  for alba in alba_list:
    # Dict 형에서 List 형으로 전환할 때 key만 가져오고 싶으면 Dict.keys() value만 가져오고 싶으면 Dict.values()
    writer.writerow(list(alba.values()))

######################################################################################################################
# 5일차
"""
보일러플레이트를 이용하여 세 종류의 웹사이트에서 정보를 긁어와 원격 직업을 찾는 "job scrapper"를 만드세요.
This is how the website should behave: https://imgur.com/DCIdYE5
웹사이트는 .csv 파일 내보내기가 가능해야 됩니다.
반복 검색 속도가 빨라지기 위해서 fakeDB를 구현해야 됩니다.
아래에 있는 세 종류의 웹사이트를 모두 스크랩해야 됩니다.
https://weworkremotely.com/
https://stackoverflow.com/jobs
https://remoteok.io/

These are the URLs that will give you remote jobs for the word 'python'
https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs
Good luck!
"""

import os
import csv
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect

""" ~~~~~~~~ HTML 파트 ~~~~~~~~ """
app = Flask("PyCh", template_folder="NOMAD_Challenge\HTML Template")

@app.route("/")
def home():
  return render_template("Flask.html")

@app.route("/report")
def report():
  text = request.args.get("text")
  text = ("+").join(list(text.split()))
  if text:
    text = text.lower()
    # Fake_DB에 해당 Text가 존재할 경우 jobs에 결과값을 바로 출력하고, 없을 경우 스크래핑 후 Fake_DB에 저장, 동일 키워드 검색 횟수로 Count_DB 사용
    if Fake_DB.get(text):
      jobs = Fake_DB[text]
      Count_DB[text] += 1
    else:
      jobs = search_all(text)
      Fake_DB[text] = jobs
      Count_DB[text] = 1
  else:
    return redirect("/")
  return render_template \
    ("Report.html", text=text,
     ResultsNumber=len(jobs), SerchingCount=Count_DB[text],
     jobs=jobs
     )

@app.route("/export")
def export():
  try:
    text = request.args.get("text")
    if not text:
      raise Exception()
    text = text.lower()
    jobs = Fake_DB.get(text)
    if not jobs:
      raise Exception()
    to_csv(jobs, text)
    return f"Generate CSV for {text}"
  except:
    return redirect("/")

""" ~~~~~~~~ 함수 파트 ~~~~~~~~ """

def search_all(Search):
  URL1st = f"https://weworkremotely.com/remote-jobs/search?term={Search}"
  URL2nd = "https://stackoverflow.com/jobs"
  URL3rd = f"https://remoteok.com/remote-{Search}-jobs"
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}

  WWR_worklist = WWR(URL1st)
  # SOF_worklist = SOF(URL2nd)
  ROK_worklist = ROK(URL3rd, headers)

  return WWR_worklist + ROK_worklist

def WWR(URL):
  results = requests.get(URL)
  soup = BeautifulSoup(results.text, 'html.parser')

  WWR = []
  big_container = soup.find("div", {"class": "jobs-container"})
  section_container = big_container.find_all("section", {"class": "jobs"})

  for i in section_container:
    features = i.find_all("li", {"class": "feature"})
    # section = i.find("a").text
    # print("#"*5,section,"#"*5,"\n")
    for j in features:
      company, contract, site = j.find_all("span", {"class": "company"})
      title = j.find("span", {"class": "title"})
      appliance = "https://weworkremotely.com" + j.find_all("a")[1]["href"]
      WWR.append(
        {
          "company": company.text,
          "title": title.text,
          "contract": contract.text,
          "site": site.text,
          "appliance": appliance
        }
      )
  return WWR

def ROK(URL, headers):
  results = requests.get(URL, headers=headers)

  soup = BeautifulSoup(results.text, 'html.parser')

  ROK = []
  jobs = soup.find_all("tr", {"class": "job"})

  for i in jobs:
    company = i.find("h3")
    title = i.find("h2")
    site_contract = i.find_all("div", {"class": "location"})
    try:
      site = site_contract[0].text
      contract = site_contract[1].text
    except IndexError:
      site = "N/A"
      contract = "N/A"
    except:
      if "location tooltip" in site_contract[0]:
        site = site_contract[0].text
        contract = "N/A"
      else:
        site = "N/A"
        contract = site_contract[0].text
    appliance = "https://remoteok.com/" + i.find("a")["href"]

    ROK.append(
      {
        "company": company.text.strip("\n"),
        "title": title.text.strip("\n"),
        "contract": contract,
        "site": site,
        "appliance": appliance
      }
    )

  return ROK

def to_csv(jobs_list, key):
  file = open(f"{key}.csv", "w")
  WR = csv.writer(file)
  WR.writerow(["company", "title", "contract", "site", "appliance"])
  for job in jobs_list:
    WR.writerow(list(job.values()))

""" ~~~~~~~~ 실행 파트 ~~~~~~~~ """
os.system("clear")

Fake_DB = {}
Count_DB = {}

app.run(host='0.0.0.0')
