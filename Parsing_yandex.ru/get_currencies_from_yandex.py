#>python d:\GitHub\CLC_Python\Parsing_yandex.ru\get_currencies_from_yandex.py

from bs4 import BeautifulSoup
import requests

r = requests.get('https://yandex.ru')
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')

a = []

for i in soup.find_all('span', attrs={'class': 'inline-stocks__value_inner'}):
   a.append(i.text.strip())

print('\nDollar rate: ' + a[0] + 'RUB')
print('Euro   rate: ' + a[1] + 'RUB\n')