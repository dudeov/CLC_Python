fhand = open('result.txt')
from bs4 import BeautifulSoup
r_html = fhand.read()
soup = BeautifulSoup(r_html, 'html.parser')

fhand2 = open('formatted_result.txt', 'w')

fhand2.write(soup.prettify())
fhand.close()
fhand2.close()

