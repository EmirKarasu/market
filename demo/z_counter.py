import requests
from bs4 import BeautifulSoup
#sorunlu hisseler
##https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=ISFIN
##https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=RAYSG
##https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=TURSG

sirketler_listesi_2=["https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=ISFIN"]

pd =input("pd giriniz: ")
for i in sirketler_listesi_2:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_td_tags = []


    for j in soup.select('td'):
        all_td_tags.append(j.text)

    #print(all_td_tags[82]) #fk
    #print(all_td_tags[84]) #pd
i=0
for k in all_td_tags:
    i += 1
    if pd in k:
        print(f"eleman {i}")
        print('yes')
        print(all_td_tags[i])
        print(all_td_tags[i-1])
        print(all_td_tags[i-3])
print(all_td_tags)
print(all_td_tags[56])
print(all_td_tags[54])

