import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook,load_workbook
sirket_kartlari = ["https://tr.investing.com/equities/aksa-enerji-uretim-ratios"]

for i in sirket_kartlari:
    page = requests.get(i).text
    soup = BeautifulSoup(page, 'html.parser')
    all_td_tags = []

    for j in soup.select('td'):
        all_td_tags.append(j.text)

    print(all_td_tags)