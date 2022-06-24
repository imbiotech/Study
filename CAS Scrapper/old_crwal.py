import requests
import csv
from time import time, sleep
from bs4 import BeautifulSoup as BS

CASLIST=[
"149182-72-9",
"136465-81-1",
"617-55-0",
"86087-23-2",
"42890-76-6",
"4726-85-1",
"109-75-1",
"87392-07-2",
"616-42-2",
"13734-34-4",
"52-51-7",
"99-34-3",
"534-03-2",
"55406-53-6",
"10601-19-1",
"16732-57-3",
"7331-52-4",
"204251-24-1",
"71989-26-9",
"109425-51-6",
"71989-23-6",
"132388-59-1",
"71989-14-5",
"132327-80-1",
"143824-78-6",
"146645-63-8",
"71989-38-3",
"71989-38-3",
"99520-81-7",
"5153-67-3",
"5535-48-8",
"504-01-8",
"2380-94-1",
"16732-57-3",
"16732-57-3",
"5535-48-8",
"71989-20-3",
"141942-85-0",
"95537-36-3",
"141942-85-0",
"71989-35-0",
"71989-33-8",
"10575-25-4",
"77497-97-3",
"57260-71-6",
"485-72-3",
"7531-52-4",
"616-44-4",
"22348-32-9",
"3068-00-6",
"99395-88-7",
"19501-58-7",
"15761-38-3",
"87776-75-8",
"6638-79-5",
"14345-97-2",
"133871-50-8",
"133871-50-8",
"132997-77-4",
"939-97-9",
"147128-77-6",
"147128-77-6",
"1193-65-3",
"98-78-2",
"14071-33-1",
"960404-59-5",
"369-34-6",
"950172-03-9",
"170810-05-6",
"18372-22-0",
"69891-92-5",
"461432-23-5",
"95510-70-6",
"425640-13-7",
"56346-57-7",
"3017-69-4",
"36076-19-4",
"179178-90-6",
"808768-95-9",
"3916-18-5",
"2436-29-5",
"129217-85-2",
"61676-62-8",
"61676-62-8",
"129217-85-2",
"140-76-1",
"140-76-1",
"66211-46-9",
"88495-54-9",
"889942-56-4",
"630423-36-8",
"1028252-11-0",
"24188-74-7",
"630423-35-7",
"20098-14-0",
"20098-14-0",
"1062580-52-2",
"35661-39-3",
"68858-20-8",
"35661-40-6",
"94744-50-0",
"1221416-42-7",
"154350-29-5",
"76193-67-4",
"883749-85-7",
"619-81-1",
"105942-09-4",
"4072-67-7",
"4072-67-7",
"15761-39-4",
"69267-75-0",
"69267-75-0",
"66673-40-3",
"94610-82-9",
"1224708-00-2",
"1269292-82-1",
"6485-55-8",
"6485-55-8",
"6485-55-8",
"1008726-80-4",
"78902-09-7",
"2913-97-5",
"1191377-84-0",
"62012-54-8",
"42969-65-3",
"121522-26-7",
"121522-26-7",
"62012-54-8",
"36635-61-7",
"15771-06-9",
"143111-65-3",
"713143-67-0",
"1008726-80-4",
"117661-72-0",
"7145-99-5",
"7145-99-5",
"40046-11-9",
"32673-41-9",
"199192-04-6",
"199192-04-6",
"85908-96-9",
"6290-49-9",
"6290-49-9",
"5000-66-8",
"913088-80-9",
"913088-80-9",
"913088-80-9",
"865774-79-4",
"843644-23-5",
"406-87-1",
"956699-05-01",
"62075-23-4",
"177944-16-0",
"623155-66-8",
"552292-58-7",
"106092-11-9",
"104617-49-4",
"1315483-31-8",
"1190363-46-2",
"605-38-9",
"39713-36-5",
"96202-57-2",
"62965-35-9",
"367-21-5",
"3685-27-6",
"4398-36-1",
"1191377-84-0",
"17269-99-7",
"1206524-85-7",
"10203-08-4",
"787-69-9",
"936643-80-0",
"34253-03-7",
"42839-09-8",
"334769-80-1",
"896733-29-2",
"676560-85-3",
"676560-83-1",
"207557-35-5",
"3680-69-1",
"52133-67-2",
"3680-71-5",
"3680-69-1",
"135655-75-3",
"678992-41-1",
"678992-41-1",
"54274-80-5",
"51135-96-7",
"191327-87-4",
"1259393-27-5",
"1259393-31-1",
"1259393-32-2",
"1259393-32-2",
"1016636-76-2",
"1190399-91-7",
"1035230-24-0",
"1369427-40-6",
"69610-41-9",
"602325-71-3",
"164456-57-9",
"179039-97-5",
"179039-97-5",
"159857-80-4",
"68858-20-8",
"159858-21-6",
"159858-22-7",
"159857-79-1",
"57079-14-8",
"55750-63-5",
"136040-19-2",
"89171-23-3",
"1228690-37-6",
"893643-73-7",
"917388-58-0",
"91182-60-4",
"52407-92-8",
"869-10-3",
"52321-07-0",
"52321-08-1",
"571188-59-5",
"775288-71-6",
"571189-16-7",
"1251033-29-0",
"1251033-29-0",
"302964-24-5",
"302964-24-5",
"209849-99-0",
"3934-20-1",
"17630-76-1",
"13096-62-3",
"1520112-88-2",
"1216965-67-1",
"1216965-66-0",
"862574-87-6",
"1282516-74-8",
"2414-98-4",
"1445961-79-4",
"1431329-07-5",
"73479-06-8",
"1092536-54-3",
"18387-63-8",
"1294504-65-6",
"1092536-54-3",
"733039-20-8",
"1187595-85-2",
"59801-62-6",
"140174-14-7",
"1425038-21-6",
"848821-58-9",
"911482-75-2",
"1032684-85-7",
"28957-33-7",
"108491-55-0",
"124932-43-0",
"1544662-09-0",
"89641-18-9",
"1240948-77-9",
"655-15-2",
"312307-38-3",
"1344-28-1",
"1508258-32-9",
"1508258-27-2",
"1508258-29-4",
"26475-62-7",
"1562245-02-6",
"478828-53-4",
"1995856-24-0",
"5267-64-1",
"104706-47-0",
"2799-21-5",
"2799-21-5",
"1433860-44-6",
"97094-17-2",
"863-61-6",
"159857-80-4",
"130878-68-1",
"159858-21-6",
"159858-22-7",
"159857-79-1",
"57079-14-8",
"55750-63-5",
"1627893-92-8",
"916806-97-8",
"13376-26-6",
"13376-27-7",
"1449291-53-5",
"7531-52-4",
"34079-31-7",
"134031-24-6",
"32384-65-9",
"1673515-13-3",
"1897428-40-8",
"5762-40-3",
"1897388-80-5",
"1897387-75-5",
"1286770-55-5",
"1877329-53-7",
"1877329-54-8",
"1877329-50-4",
"1875153-95-9",
"2245111-15-1",
"1352925-63-3",
"1817776-86-5",
"1434127-91-9",
"59767-24-7",
"194085-75-1",
"194085-75-1",
"1235479-59-0",
"80703-23-7",
"97551-10-5",
"1356460-51-9",
"1316755-17-5",
"1933460-46-8",
"462629-01-2",
"28319-77-9",
"1188302-00-2",
"1111637-77-4",
"947249-14-1",
"947249-13-0",
"1283129-18-9",
"25475-67-6",
"143782-23-4",
"254750-02-2",
"409369-36-4",
"254750-02-2",
"1979-03-08",
"1354690-24-6",
"1311254-72-4",
"914612-23-0",
"1354691-73-8",
"409369-29-5",
"1119253-07-4",
"189580-34-5",
"1802431-24-8",
"6228-73-5",
"7436-22-8",
"1897428-40-8",
"900161-12-8",
"900161-13-9",
"618385-01-6",
"705260-08-8",
"537013-51-7",
"1444535-74-3",
"1956372-62-5",
"87392-05-0",
"900161-13-9",
"654-70-6",
"1433363-42-8",
"7531-52-4",
"7531-52-4",
"57235-84-4",
"105-50-0",
"162537-11-3",
"1188302-00-2",
"1111637-77-4",
"947249-14-1",
"947249-13-0",
"274901-16-5",
"6310-21-0",
"1802425-99-5",
"1802431-24-8",
"649761-22-8",
"649761-21-7",
"649761-21-7",
"1897387-75-5",
"1897387-75-5",
"1345017-16-4",
"4254-15-3",
"4254-15-3",
"913088-80-9",
"913088-80-9",
"913088-80-9",
"18388-07-3",
"78495-63-3",
"2230200-76-5",
"1335210-23-5",
"3680-69-1",
"3680-69-1",
"649761-22-8",
"162537-11-3",
"79-22-1",
"149182-72-9",
"149182-72-9",
"136465-81-1",
"617-55-0",
"86087-23-2",
"86087-23-2",
"42890-76-6",
"87392-07-2",
"7331-52-4",
"204251-24-1",
"71989-26-9",
"109425-51-6",
"132388-59-1",
"71989-14-5",
"71989-14-5",
"132327-80-1",
"143824-78-6",
"7531-52-4",
"100-58-3",
"1221416-42-7",
"18171-11-4",
"1520113-02-3",
"147406-55-1",
"179039-97-5",
"75-64-9",
"108-88-3",
"7647-01-0",
"1310-73-2",
"67-63-0",
"110-54-3",
"142-82-5",
"64365-11-3",
"97-67-6",
"149-73-5",
"7664-93-9",
"67-56-1",
"16940-66-2",
"7647-01-0",
"144-55-8",
"25322-68-3",
"6192-52-5",
"68855-54-9",
"1975-09-02",
"7757-82-6",
"30525-89-4",
"7664-41-7",
"7487-88-9",
"7647-14-5",
"64-19-7",
"57-55-6",
"67-68-5",
"1968-12-02",
"7719-09-07",
"1310-58-3",
"141-78-6",
"16874-33-2",
"71-36-3",
"39389-20-3",
"530-62-1",
"121-44-8",
"110-85-0",
"584-08-7",
"75-36-5",
"123-91-1",
"82911-69-1",
"501-53-1",
"24424-99-5",
"75-78-5",
"76-83-5",
"67-64-1",
"109-99-9",
"1493-13-6",
"497-19-8",
"1336-21-6",
"73-22-3",
"1975-05-08",
"147-85-3",
"344-25-2",
"1122-58-3",
"108-24-7",
"124-63-0",
"77-92-9",
"5949-29-1",
"81133-21-3",
"110-82-7",
"75-75-2",
"7681-52-9",
"699-12-7",
"149182-72-9",
"7757-83-7",
"17199-29-0",
"541-41-3",
"74163-81-8",
"104-15-4",
"64-17-5",
"5470-11-01",
"7087-68-5",
"108-59-8",
"108-86-1",
"7439-89-6",
"124-41-4",
"7447-41-8",
"1343-98-2",
"7446-70-0",
"98-95-3",
"79-22-1",
"12125-02-9",
"7439-95-4",
"110-89-4",
"110-86-1",
"98-59-9",
"7758-89-6",
"7646-85-7",
"107-21-1",
"79-37-8",
"7697-37-2",
"100-52-7",
"141-52-6",
"74-88-4",
"141-97-9",
"4637-24-5",
"41233-93-6",
"383-63-1",
"7758-11-04",
"865-47-4",
"1975-12-07",
"872-50-4",
"7775-14-6",
"7664-38-2",
"77-78-1",
"10213-10-2",
"7778-77-0",
"7631-90-5",
"3282-30-2",
"124-38-9",
"109-63-7",
"53-84-9",
"56-81-5",
"50-81-7",
"108-94-1",
"100-63-0",
"5891-21-4",
"3159-07-07",
"121-69-7",
"109-77-3",
"407-25-0",
"107-93-7",
"7722-84-1",
"127-19-5",
"108-31-6",
"308080-99-1",
"42969-65-3",
"107-02-8",
"65-85-0",
"298-12-4",
"21369-64-2",
"999-97-3",
"288-32-4",
"108-21-4",
"141-82-2",
"109-02-4",
"123-75-1",
"7681-57-4",
"67843-74-7",
"104-88-1",
"90-80-2",
"75-77-4",
"7558-80-7",
"109-72-8",
"631-61-8",
"110-65-6",
"1310-66-3",
"7440-44-0",
"53990-33-3",
"1125-88-8",
"373-61-5",
"7226-23-5",
"10035-10-6",
"4039-32-1",
"298-14-6",
"40949-94-8",
"110-16-7",
"1779-49-3",
"1070-89-9",
"16029-98-4",
"98-79-3",
"630-19-3",
"80-73-9",
"107-31-3",
"7727-73-3",
"504-63-2",
"603-35-0",
"16853-85-3",
"69912-79-4",
"21739-92-4",
"617-86-7",
"103-73-1",
"27607-77-8",
"7786-30-3",
"3430-27-1",
"96-47-9",
"616-38-6",
"64365-11-3",
"7440-44-0",
"56553-60-7",
"128-37-0",
"3473-63-0",
"3886-69-9",
"2564-83-2",
"7649-15-6",
"7772-98-7",
"288-94-8",
"3240-34-4",
"7499-06-01",
"2743-38-6",
"1189-71-5",
"220032-26-8",
"200004-39-3",
"7681-11-0",
"7778-53-2",
"1191-15-7",
"563-47-3",
"7790-86-5",
"14221-01-3",
"142-82-5",
"63132-85-4",
"64-18-6",
"125700-67-6",
"127-09-3",
"144-62-7",
"865-48-5",
"128-08-5",
"24292-60-2",
"762-04-9",
"787-69-9",
"7726-95-6",
"148893-10-1",
"10102-17-7",
"7647-01-0",
"5419-55-6",
"1634-04-4",
"100-46-9",
"75-31-0",
"12135-22-7",
"108-18-9",
"7681-82-5",
"7761-88-8",
"1976-05-01",
"2032-35-1",
"102-71-6",
"100-39-0",
"1074-82-4",
"20781-20-8",
"96-26-4",
"121-43-7",
"126-30-7",
"2142-68-9",
"7727-21-1",
"4648-54-8",
"429-41-4",
"540-69-2",
"627-27-0",
"7440-66-6",
"1119-40-0",
"89-00-9",
"80522-42-5",
"3375-31-3",
"27514-08-5",
"937-14-4",
"506-87-6",
"151-50-8",
"3731-51-9",
"17159-79-4",
"10035-10-6",
"62-56-6",
"147-71-7",
"7631-90-5",
"280-57-9",
"500-05-0",
"96-50-4",
"123536-14-1",
"51-35-4",
"20859-02-3",
"288-47-1",
"14464-66-4",
"6674-22-2",
"39267-04-4",
"74844-91-0",
"7681-65-4",
"13965-03-2",
"350-30-1",
"99-90-1",
"7647-10-01",
"15761-39-4",
"144978-12-1",
"26386-88-9",
"60676-86-0",
"1979-04-09",
"7531-52-4",
"14080-23-0",
"105-56-6",
"14593-46-5",
"82380-18-5",
"1013-88-3",
"2106-05-0",
"7440-44-0",
"1259393-22-0",
"1003-03-8",
"36082-50-5",
"7440-44-0",
"1032903-62-0",
"1571-08-0",
"24057-28-1",
"16731-55-8",
"10139-58-9",
"79099-07-3",
"100-44-7",
"1517-69-7",
"7447-40-7",
"5614-37-9",
"344-04-7",
"3984-14-3",
"1670-82-2",
"87-56-9",
"87-63-8",
"586-75-4",
"1774-47-6",
"96202-57-2",
"7507-86-0",
"105-53-3",
"66-22-8",
"124-04-9",
"74-89-5",
"112926-00-8",
"4132-28-9",
"26412-87-3",
"7789-23-3",
"1719-57-9",
"77-76-9",
"109-01-3",
"40465-45-0",
"68957-94-8",
"95-54-5",
"1344-28-1",
"578-57-4",
"28320-31-2",
"4045-44-7",
"7550-45-0",
"140-66-9",
"546-68-9",
"13292-87-0",
"512-56-1",
"22348-32-9",
"311-28-4",
"3144-16-9",
"12112-67-3",
"135139-00-3",
"39389-20-3",
"5535-48-8",
"52092-47-4",
"20769-85-1",
"112-71-0",
"86-73-7",
"7550-45-0",
"917-54-4",
"108-87-2",
"60-29-7",
"571189-16-7",
"420-37-1",
"20734-58-1",
"69610-40-8",
"96-33-3",
"29858-07-9",
"123-46-6",
"101-83-7",
"1619-34-7",
"623-04-1",
"60-32-2",
"372-75-8",
"538-75-0",
"16357-59-8",
"68858-20-8",
"543-27-1",
"6066-82-6",
"1113-59-3",
"2414-98-4",
"80-70-6",
"105942-08-3",
"7631-86-9",
"70629-60-6",
"5272-33-3",
"12129-06-5",
"16726-41-3",
"3587-60-8",
"123-90-0",
"938-09-0",
"106454-69-7",
"1092536-54-3",
"112068-01-6",
"7553-56-2",
"124-43-6",
"2675-89-0",
"109-76-2",
"5162-44-7",
"13161-30-3",
"122-52-1",
"3057-74-7",
"39416-48-3",
"1068-55-9",
"53064-79-2",
"1184-16-3",
"107-05-1",
"911482-75-2",
"4394-85-8",
"111-96-6",
"70955-01-0",
"7440-44-0",
"64365-11-3",
"1544665-31-7",
"2971-79-1",
"17476-04-9",
"56686-16-9",
"868-85-9",
"445-27-2",
"75-89-8",
"7646-93-7",
"7274-88-6",
"110-71-4",
"7440-44-0",
"7440-44-0",
"506-68-3",
"9004-34-6",
"93763-70-3",
"540-51-2",
"1259059-71-6",
"53857-57-1",
"110-87-2",
"1072-98-6",
"7752-82-1",
"40235-68-5",
"182344-16-7",
"132705-51-2",
"694-59-7",
"564483-18-7",
"673-06-3",
"51364-51-3",
"930-68-7",
"148719-91-9",
"708-76-9",
"112-55-0",
"111865-47-5",
"78-95-5",
"123927-75-3",
"98-54-4",
"25952-53-8",
"90319-52-1",
"35963-20-3",
"541-16-2",
"391-77-5",
"1068-55-9",
"392-83-6",
"77-48-5",
"62965-35-9",
"26452-80-2",
"1070-89-9",
"694495-63-1",
"18618-55-8",
"80-62-6",
"79-46-9",
"9001-62-1",
"7440-02-0",
"126-33-0",
"2158-14-7",
"105-50-0",
"7550-35-8",
"998-40-3",
"126-33-0",
"67579-81-1",
"107-15-3",
"27192-21-8",
"151-10-0",
"108-00-9",
"72072-19-6",
"13472-35-0",
"461432-22-4",
"15128-82-2",
"1895-39-2",
"127-08-2",
"72287-26-4",
"73183-34-3",
"57090-45-6",
"72556-74-2",
"103591-11-3",
"7440-44-0",
"255837-19-5",
"1979-03-08",
"616-91-1",
"75-85-4",
"2491-20-5",
"6310-21-0",
"2052-49-5",
"26048-69-1",
"769-39-1",
"42289-34-9",
"3470-98-2",
"1336-21-6",
"216854-23-8",
"864293-36-7",
"838-85-7",
"23147-57-1",
"865-47-4",
"590-93-2",
"344-14-9",
"867-44-7",
"7601-54-9",
"64365-11-3",
"78-39-7",
"41468-25-1",
"4023-34-1",
"18197-26-7",
"811-98-3",
"98-59-9",
"69-72-7",
"65-45-2",
"619-67-0",
"75-31-0",
"25952-53-8",
"461-96-1",
"52950-19-3",
"116-11-0",
"16949-15-8",
"128-09-6",
"53014-84-9",
"54716-02-8",
"7440-44-0",
"1330-20-7",
"64-17-5",
"110-86-1",
"7803-49-8",
"4132-28-39",
"616-47-7",
"2524-64-3",
"77-98-5",
"108-48-5",
"15128-82-2",
"20989-17-7",
"7632-00-0",
"105-58-8",
"75-65-0",
"7632-00-0",
"26628-22-8",
"1968-12-02",
"7531-52-4",
"78-93-3",
"108-21-4",
"702-82-9",
"1979-04-09",
"3724-43-4",
"584-08-7",
"67-63-0",
"1634-04-4",
"7681-11-0",
"6674-22-2",
"7440-44-0",
"1188-21-2",
"3430-14-6",
"7440-16-6",
"131878-23-4",
"456-49-5",
"150-46-9",
"10294-33-4",
"1344-28-1",
"716-61-0",
"1345017-16-4",
"7440-44-0",
"1310-73-2",
"27871-49-4",
"768-33-2",
"79-36-7",
"1309-42-8",
"7727-37-9",
"1333-74-0",
"22483-09-6",
"553-90-2",
"41051-15-4",
"1310-65-2",
"3680-71-5",
"3680-71-5",
"1245643-11-1",
"30379-55-6",
"55750-63-5",
"159857-79-1",
"461432-23-5",
"1259059-71-6",
"108-88-3",
"108-88-3",
"109-52-4",
"10025-87-3",
"7647-01-0",
"1310-73-2",
"1310-73-2",
"1310-73-2",
"142-82-5",
"10049-08-8",
"64365-11-3",
"7664-93-9",
"67-56-1",
"67-56-1",
"67-56-1",
"16940-66-2",
"7647-01-0",
"74-98-6",
"25322-68-3",
"1975-09-02",
"7647-14-5",
"1968-12-02",
"141-78-6",
"121-44-8",
"110-85-0",
"584-08-7",
"584-08-7",
"123-91-1",
"123-91-1",
"67-64-1",
"109-99-9",
"1336-21-6",
"1975-05-08",
"1975-05-08",
"147-85-3",
"147-85-3",
"147-85-3",
"7681-52-9",
"109-89-7",
"64-17-5",
"124-41-4",
"676-58-4",
"41233-93-6",
"865-47-4",
"872-50-4",
"872-50-4",
"108-94-1",
"308080-99-1",
"108-21-4",
"109-02-4",
"90-80-2",
"109-72-8",
"109-72-8",
"16853-85-3",
"3886-69-9",
"142-82-5",
"787-69-9",
"52092-47-4",
"42890-76-6",
"1975-09-02",
"67-64-1",
"64-17-5",
"7631-90-5",
"125700-67-6",
"34079-31-7",
"1310-73-2",
"174813-82-2",
"7803-57-8",
"18871-66-4",
"1310-73-2",
"380894-77-9",
"2106-49-2",
"4111-54-0",
"106-96-7",
"96-30-0",
"77-78-1",
"1956-05-03",
"2516-47-4",
"3473-63-0",
"127852-28-2",
"2106-49-2",
"1346145-51-4",
"34825-81-5",
"499796-71-3",
"117-34-0",
"3939-01-03",
"147081-44-5",
"1214377-42-0",
"1897387-75-5",
"1802430-55-2",
"254750-02-2",
"274901-16-5",
"201530-41-8",
"274901-16-5",
"201530-41-8",
"201530-41-8",
"1802430-55-2",
"452-72-2",
"1793080-77-9",
"2198942-41-3",
"1245643-11-1",
"30379-55-6",
"950172-03-9",
"2230200-76-5",
"1344-28-1",
"12257-42-0",
"494227-37-1",
"7732-18-5"]

# openw1_csv = open(r"a.csv","w", -1,'utf-8', newline="") #작성 리스트 a 생성
# write1_csv = csv.writer(openw1_csv)

i=len(CASLIST)

for cas in CASLIST:
    URL1=f"https://www.chemicalbook.com/CASEN_{cas}.htm"
    lists = []
    result=requests.get(URL1)
    soup=BS(result.text,'html.parser')
    contentholder = soup.find_all("td", {"colspan": "2"})
    for context in contentholder[:-2]:
        cont = context.text
        cont_right = cont.find("]")+1
        key = cont[1:cont_right-1].replace("\xa0","")
        value = cont[cont_right:].replace("\xa0","")
        lists.append({key:value})
    print(lists)
    sleep()

    URL2=f"https://www.chemblink.com/products/{cas}.htm"




#     res2=requests.get(url2) #url로부터 정보 획득
#     c2=res2.content
#     soup2=BS(c2,'html.parser')
#
#     second = soup2.select("td > table > tr > td",class_="style2")
#     j = len(second)
#     l = ""
#     if j != 0:
#         for k in range(j):
#             l += second[k].text.strip()
#     write2_csv.writerow(l)
#
#     # url 3
#     URL3=f"https://www.capotchem.com/{cas}.html"
#     res3=requests.get(url3) #url로부터 정보 획득
#     c3=res3.content
#     soup3=BS(c3,'html.parser')
#     third = soup3.select("span > li > p")
#     j = len(third)
#     l = ""
#     if j != 0:
#         for k in range(j):
#             l += third[k].text.strip()
#     write3_csv.writerow(l)
#
#     #진행률
#     print("{} of {} ({}%)".format(i,lines,round(i/lines*100,2)))
#     i+=1
#
#     #시간 지연
#     time.sleep(5)
#
# openr_csv.close()
# openw1_csv.close()
# openw2_csv.close()
# openw3_csv.close()
#
# print("END") #종료
# raw_input()



"""
url = 'https://www.chemicalbook.com/CASEN_149182-72-9.htm'
res = requests.get(url)
c = res.content
soup = BeautifulSoup(c, 'html.parser')
# print(soup.select("#ContentPlaceHolder1_SubClass > table > tr > td").get_text())
print(soup.find_all('br'))
write_csv.writerow(soup.find_all('br'))
"""


