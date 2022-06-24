import requests
from bs4 import BeautifulSoup as BS

# 동적 페이지 스크래핑

URL = "https://www.kbiois.or.kr/portal/bioCompany/bioCompanyList.do"
headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36",
"referer":"https://www.kbiois.or.kr/portal/bioCompany/bioCompanyPage.do"
}


# results = requests.get(URL, headers=headers)
results = requests.post(URL, headers=headers)
if results.status_code == requests.codes.ok:
  print("접속 완료")
# print(results.text)

soup = BS(results.text, 'html.parser')

print(soup)


#  = soup.find("div", {"class": "jobs-container"})
# section_container = big_container.find_all("section", {"class": "jobs"})