from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def make_soup(url):
	html = urlopen(url).read()
	return BeautifulSoup(html)

def get_images(url):
	soup = make_soup(url)

	images = [img for img in soup.findAll('img')]
	print (str(len(images)) + "images found.")
	print 'Downloading images to current working directory.'
	#compile our unicode list of image links
	image_links = [each.get('src') for each in images]
	for each in image_links:
		filename=each.split('/')[-1]
		urllib.urlretrieve(each, filename)
	return image_links

get_images('https://www.lfc.pl')
