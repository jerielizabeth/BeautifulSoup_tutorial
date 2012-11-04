from bs4 import BeautifulSoup

soup = BeautifulSoup (open("43rd-congress.txt"))

clean_list = []
links = soup.find_all('a')
for link in links:	
	single_link = link['href']
	Name = link.contents[0]
	entry = "%s, %s" % (Name, single_link)
	clean_list.append(entry)

f = open("43rd_results.csv", "w")
f.write("\n".join(clean_list))
f.close
		
