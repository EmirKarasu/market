import requests
from bs4 import BeautifulSoup


sirketler_listesi_2=["https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=TAVHL",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=TCELL",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=THYAO",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=TKFEN",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=TOASO",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=TTKOM",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=TTRAK",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=SELEC",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=SAHOL",
                     "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=SISE"
                     ]


for i in sirketler_listesi_2:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_td_tags = []


    for j in soup.select('td'):
        all_td_tags.append(j.text)

    print(all_td_tags[82]) #fk
    print(all_td_tags[84]) #pd
    #print(all_td_tags)