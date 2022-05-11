import csv
from CAS_Scrapper_F import purification, url1
import time

#시간 입력
start = time.time()

# Text File 읽기, 머릿글 삭제, 개행 문자 삭제
notepad = open("CAS_ANSI.txt", 'r')
csv_file1 = open("CAS_Result.csv","w",encoding="utf-8",newline="")
csv_file1_writer = csv.writer(csv_file1)
cas_list = notepad.readlines()
purified = purification(cas_list)

# URLs
count=1
csv_file1_writer.writerow(["Name","CAS","Formula","MW","MP","BP","Density"])
for cas in purified:
    print(f"Working.... {count} / {len(purified)}")
    count += 1

    URL1 = f"https://www.chemicalbook.com/CASEN_{cas}.htm"
    csv_file1_writer.writerow(url1(URL1, cas))

print("Works Done!")

# 시간 출력
delay = round(time.time()-start,0)
if delay // 3600 > 0:
    print(delay // 3600, "h", (delay // 3600 // 60), "m",  (delay // 3600 // 60 // 60), "s")
else:
    if delay // 60 > 0:
        print((delay // 3600 // 60), "m", (delay // 3600 // 60 // 60), "s")
    else:
        print((delay // 3600 // 60 // 60), "s")
