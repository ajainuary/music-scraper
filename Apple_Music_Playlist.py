import requests
from bs4 import BeautifulSoup
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
pl_list = soup.find('ul', class_='tracklist')
pl = pl_list.find_all('div', class_='tracklist-item__text')
for song in pl:
	for x in song.stripped_strings:
		print(x, end=" ")
	print()