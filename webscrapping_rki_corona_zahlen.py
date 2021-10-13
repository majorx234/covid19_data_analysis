from bs4 import BeautifulSoup
import requests
import csv
from datetime import date

today = str(date.today())

domain = 'https://www.corona-daten-deutschland.de'
relative_path = '/dataset/todesfaelle'

inhalt_seite = requests.get(domain + relative_path).content

soup = BeautifulSoup(inhalt_seite , 'html.parser')

anchor_tag = soup.select_one('a[class="heading"]')#.get_text(strip=True)

todesfaelle_link = domain + anchor_tag['href']

inhalt_todesfaelle = requests.get(todesfaelle_link).content

soup_todesfaelle = BeautifulSoup(inhalt_todesfaelle , 'html.parser')

a_class = "btn btn-primary resource-url-analytics resource-type-datastore"

anchor_tag_csv = soup_todesfaelle.select_one('a[class="'+a_class+'"]')

download_csv = anchor_tag_csv['href']

csv_req = requests.get(download_csv)
url_content = csv_req.content
csv_file = open('Todesfaelle_Corona_'+ today +'.csv', 'wb')

csv_file.write(url_content)
csv_file.close()

#print(download_csv)
