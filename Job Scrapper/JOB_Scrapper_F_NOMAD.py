import requests
from bs4 import BeautifulSoup
import csv


def extract_pages(URL):
    results = requests.get(URL)
    soup = BeautifulSoup(results.text, 'html.parser')
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]

    return max_page


def extract_jobs(last_page, URL, LIMIT):
    jobs = []

    for page in range(last_page):
        print(f"On-going at page {page + 1}")
        result = requests.get(f"{URL}&start={last_page * LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "slider_item"})

        for link in results:
            job = extract_data(link)
            jobs.append(job)

    return jobs


def extract_data(link):
    jobtitle = link.find("h2", {"class": "jobTitle"})
    jobtitle_anchors = jobtitle.find_all("span")

    if jobtitle_anchors[0].string == "new":
        jobtitle = jobtitle_anchors[1].string
    else:
        jobtitle = jobtitle.string

    companyname = link.find("span", {"class": "companyName"})
    companyname_anchor = companyname.find("a")

    if companyname_anchor is not None:
        companyname = companyname_anchor.string
    else:
        companyname = companyname.string

    location = link.find("div", {"class": "companyLocation"})
    location_plus = location.text.find("+")

    if location.string is None:
        if location_plus < 0:
            location = location.text
        else:
            location = location.text[0:location_plus]
    else:
        location = location.string

    return {"title": jobtitle, "company": companyname, "location": location}


def get_indeed_jobs(text):
    LIMIT = 50
    URL = f"http://www.indeed.com/jobs?q={text}&limit={LIMIT}"

    last_page = extract_pages(URL)
    jobs = extract_jobs(last_page, URL, LIMIT)

    return jobs


def exporter_csv(jobs):
    file = open("D:\Python\pj\Job_result.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        # Dict 형에서 List 형으로 전환할 때 key만 가져오고 싶으면 Dict.keys() value만 가져오고 싶으면 Dict.values()
        writer.writerow(list(job.values()))
    return


# 네이버 블로그 스크래핑
import requests
from bs4 import BeautifulSoup
URL="https://blog.naver.com/네이버아이디/게시글번호"
result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
URL_blog = "https://blog.naver.com/"+soup.find("iframe")["src"]
print(URL_blog)
result2 = requests.get(URL_blog)
soup2 = BeautifulSoup(result2.text, "html.parser")
data = soup2.find("div", {"class": "se-main-container"})
print(data.text)