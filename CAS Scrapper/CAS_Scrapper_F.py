import requests
from bs4 import BeautifulSoup

# 머릿글 삭제, 개행 문자 삭제
def purification(list):

    list.remove(list[0])

    purified_list = []
    for data in list:
        data = data[0:-1]
        purified_list.append(data)

    return purified_list

# Chem Book에서 출력
def url1(URL, cas):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    whole_data = soup.find("div",{"id":"ContentPlaceHolder1_SubClass"})
    properties = whole_data.find_all("tr")

    return extract_properties_url1(properties,cas)


# Chem Book에서 출력
def url1(URL, cas):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    whole_data = soup.find("div",{"id":"ContentPlaceHolder1_SubClass"})
    properties = whole_data.find_all("tr")

    return extract_properties_url1(properties,cas)



# Property를 List 형으로 반환, 없을 경우 Cas no.만 반환
def extract_properties_url1(properties,cas):

    # 변수 초기화
    cas_name, cas_formula, cas_weight, cas_mp, cas_bp, cas_density = "", "", "", "", "", ""

    # 헤더에 따라서 적절한 위치에 데이터 삽입
    for property in properties:
        prop_txt = property.text
        prop_find = prop_txt.find("]")
        if "[Name" in prop_txt:
            cas_name = prop_txt[prop_find + 1:]
            cas_name = cas_name.replace(",","!!")
        elif "Formula" in prop_txt:
            cas_formula =  prop_txt[prop_find + 1:]
        elif "Weight" in prop_txt:
            cas_weight = prop_txt[prop_find + 1:]
        elif "[mp" in prop_txt or "[Melt" in prop_txt :
            cas_mp = prop_txt[prop_find + 1:]
            cas_mp = del_unicode(cas_mp)
        elif "[bp" in prop_txt or "[Boil" in prop_txt:
            cas_bp = prop_txt[prop_find + 1:]
            cas_bp = del_unicode(cas_bp)
        elif "[density" in prop_txt:
            cas_density = prop_txt[prop_find + 1:]
            cas_density = del_unicode(cas_density)

    return([cas+"!", cas_name, cas_formula, cas_weight, cas_mp, cas_bp, cas_density])

# 특수 문자 정리
def del_unicode(text):
    text = text.replace("°","")
    text = text.replace("\xa0","")
    text = text.replace("±","+-")
    return text

