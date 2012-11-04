from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.txt"))

print(soup.get_text())