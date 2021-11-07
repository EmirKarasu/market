import requests
from bs4 import BeautifulSoup


sirketler_listesi_1=["https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=TUKAS"
                     ]

for i in sirketler_listesi_1:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_td_tags = []


    for j in soup.select('td'):
        all_td_tags.append(j.text)
    print(all_td_tags)
    print(all_td_tags[56]) #fk
    print(all_td_tags[54]) #pd
        #print(all_td_tags)