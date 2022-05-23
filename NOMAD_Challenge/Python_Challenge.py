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
      # 1xx - informational
      # 2xx - success
      # 3xx - redirection
      # 4xx - client error
      # 5xx - server error
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

# goodsBox
# <li class="impact">
#   <div class="B_MyAd_"></div>
#   <a class="goodsBox-info" href="http://yoogane.alba.co.kr/">
#     <span class="logo">
#       <img alt="유가네닭갈비" src="//image-logo.alba.kr/data_image2/logo/brand/20210315122240299.gif"/>
#     </span>
#     <span class="company">유가네닭갈비</span>
#     <span class="title">
#       <span>매장 아르바이트/직원 채용</span>
#     </span>
#     <span class="wrap">
#       <span class="local">전국</span>
#       <span class="pay">
#         <span class="payLetter">공고별 확인</span>
#         <span class="payIcon talk"></span>
#       </span>
#     </span>
#   </a>
# </li>
# goodslist
# <tr class="divide">
#   <td class="local first" scope="row">
#     <div class="L_MyAd_"></div>
#     경기 안성시
#   </td>
#   <td class="title">
#     <a class="" href="/job/Detail.asp?adid=113909141&amp;areacd=&amp;workaddr1=&amp;workaddr2=&amp;jobkind=&amp;jobkindsub=&amp;jobkindmulti=&amp;gendercd=&amp;agelimitcd=&amp;agelimit=0&amp;worktime=&amp;weekdays=&amp;searchterm=&amp;paycd=&amp;paystart=&amp;payend=&amp;workperiodcd=&amp;workstartdt=&amp;workenddt=&amp;workchkyn=&amp;workweekcd=&amp;targetcd=&amp;streetunicd=&amp;streetstationcd=&amp;unicd=&amp;schnm=&amp;schtext=&amp;orderby=freeorder&amp;acceptmethod=&amp;eleccontract=&amp;careercd= &amp;lastschoolcd=&amp;welfarecd=&amp;careercdunrelated=&amp;lastschoolcdunrelated=&amp;strAreaMulti=&amp;genderunrelated=&amp;special=&amp;hiretypecd=&amp;totalCount=165&amp;listmenucd=BRANDSITE">
#       <span class="company"> 플레이타임그룹 스타필드 안성점 상상스</span>
#       <span class="title">스타필드 안성점 상상스케치(어린이 만들기카페) 평일/주말 아르바이트 모집</span>
#     </a>
#     <span class="funcBtn">
#       <a class="applBtn scrap" href="javascript:void(0);" id="joblistscrapgen113909141" onclick="if( confirm('개인회원으로 로그인 후 이용 가능한 서비스입니다.\n지금 로그인 하시겠습니까?') ) { loginPerson('/job/brand/main.asp', ''); }">
#         스크랩
#       </a>
#       <a class="applBtn thumbView" href="#" id="JobFreeListTd113909141" onclick="JobPreview.PREVIEW('JobFreeList','113909141',''); return false;">
#         요약보기
#       </a>
#       <a class="applBtn blankView" href="/job/Detail.asp?adid=113909141&amp;areacd=&amp;workaddr1=&amp;workaddr2=&amp;jobkind=&amp;jobkindsub=&amp;jobkindmulti=&amp;gendercd=&amp;agelimitcd=&amp;agelimit=0&amp;worktime=&amp;weekdays=&amp;searchterm=&amp;paycd=&amp;paystart=&amp;payend=&amp;workperiodcd=&amp;workstartdt=&amp;workenddt=&amp;workchkyn=&amp;workweekcd=&amp;targetcd=&amp;streetunicd=&amp;streetstationcd=&amp;unicd=&amp;schnm=&amp;schtext=&amp;orderby=freeorder&amp;acceptmethod=&amp;eleccontract=&amp;careercd= &amp;lastschoolcd=&amp;welfarecd=&amp;careercdunrelated=&amp;lastschoolcdunrelated=&amp;strAreaMulti=&amp;genderunrelated=&amp;special=&amp;hiretypecd=&amp;totalCount=165&amp;listmenucd=BRANDSITE" target="_blank">
#         새창보기
#       </a>
#     </span>
#   </td>
#   <td class="data">
#     <span class="consult">시간협의</span>
#   </td>
#   <td class="pay">
#     <span class="payIcon hour">시급</span>
#   <br/>
#     <span class="number">9,660</span>
#   </td>
#   <td class="regDate last">
#     <strong>1시간전</strong>
#   </td>
# </tr>