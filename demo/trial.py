import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=AKSEN")
soup = BeautifulSoup(page.content, 'html.parser')

all_th_tags = []
all_tb_tags = []
all_tr_tags = []

for element in soup.select('th'):
    all_th_tags.append(element.text)

for i in soup.select('td'):
    all_tb_tags.append(i.text)

for d in soup.select('tr'):
    all_tr_tags.append(d.text)

# Create seventh_p_text and set it to 7th p element text of the page

#print(all_th_tags)
#print(all_tb_tags)
#print(all_tr_tags)
liste = []
for k in all_tr_tags:
    #print(k)
    if "PD/DD" in k:
        print(k)
        liste.append(k)
        print(liste)


#print(len(all_tb_tags))
#print(len(all_th_tags))
#print(len(all_tr_tags))

