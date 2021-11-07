import requests
from bs4 import BeautifulSoup


sirketler_listesi_2=["https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=ISFIN",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=RAYSG",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=TURSG"]
## https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=ISFIN
## https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=RAYSG
##https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=TURSG

for i in sirketler_listesi_2:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_td_tags = []


    for j in soup.select('td'):
        all_td_tags.append(j.text)

    print(all_td_tags[71]) #fk
    print(all_td_tags[69]) #pd
    print(all_td_tags)