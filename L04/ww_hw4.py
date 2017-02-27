#!/usr/bin/env python

"""HW4 for CUNY 602:  Advanced Programming Techniques, Spring 2017

__author__= 'Walt Wells'"""

from urllib import urlopen
from bs4 import BeautifulSoup
from watson_developer_cloud import AlchemyLanguageV1
from prettytable import PrettyTable

### file named 'key.py' with API key stored in variable called 'key' in same dir
from key import key


def gettext(url, attrs): 
	"""take url and desired attr tag to subset and get text.  """

	f = urlopen(link)
	website = f.read()
	f.close()
	soup = BeautifulSoup(website, 'html.parser')
	text = soup.find('div',attrs=attrs).get_text()
	return text


def APIcall(text, api_key):
    """send query to Alchemy API to return ranked keywords in json"""

    APIquery = AlchemyLanguageV1(api_key=api_key)
    json = APIquery.keywords(text)
    keywords = json['keywords']
    return keywords


def keytable(key):
    """uses PrettyTable module to return top 10 keywords w/ relevance

    PrettyTable module documentation at: https://code.google.com/archive/p/prettytable/"""

    t = PrettyTable(['Keyword', 'Relevance'])
    for i in key[0:10]:
    	t.add_row([i['text'], i['relevance']])
    return t


if __name__ == '__main__':
	
	api_key=key
	link = 'https://fivethirtyeight.com/features/cancer-rates-are-dropping-but-not-in-rural-appalachia/'
	attrs = {"class" : "entry-content single-post-content"}
	
	text = gettext(link, attrs)
	key = APIcall(text, api_key)
	table = keytable(key)
	print table
