# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import sys
from sys import argv

def write_to_file(file_name,text):
     f = open(file_name,'a')
     f.write(text)
     f.close()

def get_fh(ny_name):
	fh_info = {}
	
	url = 'http://www.cnbazi.com/'+ ny_name 
	#print url
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
	"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Accept-Encoding": "gzip, deflate",
	"Connection": "keep-alive",
	}

	try:
		html = requests.get(url)
	except requests.exceptions.ConnectionError,e:
		html = requests.get(url,headers=headers)
	if html.status_code == 200 :
		text = html.content
		Soup = BeautifulSoup(text,"html.parser")
#		print Soup
		all_fh = Soup.find('div',class_='wrap loadimg avlist-small').find_all('li')

		for fh in all_fh:
			fh_img = fh.find('img')['src']
			fh_name = fh.find('h3').text
			fh_time = fh.find_all('p')[1].text
	#		print fh_img
			fh_info[fh_name] = fh_time
	if html.status_code != 200:
		print html.status_code
	return fh_info

if __name__ == '__main__':
	ny_name = argv[1]
	print get_fh(ny_name)