from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.html"))

final_link = soup.p.a
final_link.decompose()

people = soup.find_all('a')

for p in people:
	entry = str(p)
	entry += '\n'
	
	f=open("43rd-congress.txt", "a")
	f.write(entry)
	f.close