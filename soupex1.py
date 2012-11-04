from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.html"))

print(soup.prettify())