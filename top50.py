from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen
import sys
from tqdm import tqdm

while 1:
    year = input('Enter the year you want to lookup top 50 movies for: \n')
    try:
        y = int(year)
        break
    except ValueError:
        print('Please enter a valid number for year.')
        continue

filename = 'top50movies_'+year+'.txt'
url = 'http://www.imdb.com/search/title?release_date='+year+','+year+'&title_type=feature'

print('Connecting to IMDB..')
client = urlopen(url)
page = client.read()
client.close()

print('Connection Successful. Reading data from IMDB.')
page_soup = Soup(page, 'html.parser')
titles = page_soup.findAll('h3', class_="lister-item-header")

if len(titles) == 0:
    print('IMDB has no data for that year. Exiting..')
    sys.exit()

print('Retrieving the list of most popular movies for year '+year)
title_list = list()
for title in tqdm(titles):
    title_list.append(title.a.contents[0])

print('Writing the list of movies to '+filename)
f = open(filename, 'w')
for i in tqdm(title_list):
    f.write(i+'\n')
f.close()



