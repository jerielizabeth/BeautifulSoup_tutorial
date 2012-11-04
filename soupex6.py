from bs4 import BeautifulSoup
import codecs
import csv

soup = BeautifulSoup(open("43rd-congress.html"))

#finding content

names_with_links = []
years = []
positions = []
parties = []
states = []
congress = []

links = []
names = []

rogue = soup.find(bgcolor="#990000")
rogue.decompose()

trs = soup.find_all("tr")

for tr in trs:
	tds = tr.find_all("td")
	#print tds
	try:
		names_with_links.append(tds[0])
		years.append((tds[1]).contents)
		positions.append(tds[2].contents)
		parties.append(tds[3].contents)
		states.append(tds[4].contents)
		congress.append(tds[5].contents)

	except:
		print "bad tr string"

names_object = "".join(str(names_with_links))
new_soup = BeautifulSoup(names_object)

find_links = new_soup.find_all('a')
for link in find_links:	
	single_link = link['href']
	Name = link.contents[0]
	entry1 = "%s" % (single_link)
	entry2 = "%s" % (Name)
	links.append(entry1)
	names.append(entry2)

zipped = zip(names, years, positions, parties, states, congress, links)
w = csv.writer(file("output.csv", "w"))
some_values = zipped
w.writerows(some_values)