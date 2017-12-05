# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from sys import argv


def get_cl(fh_name,max_num):
	magnetlist=[]
	url = "http://www.sosobt.net/s/" + fh_name
	html = requests.get(url)
	html = html.content
	all_magnet = re.findall(r'"magnet:?.+?"',html)
	i = 0
	max_num = 2
	if len(all_magnet) != 0:
		for magnet in all_magnet:
			i = i + 1
			if i < max_num:
				magnet = re.match(r'"(.*)"',magnet).group(1)
				magnetlist.append(magnet)
		return magnetlist
	else:
		url = "https://www.zhongzidi.com/list/" + fh_name + "/1"
		html = requests.get(url)
		html = html.content
		all_magnet = re.findall(r'"magnet:?.+?"',html)
		if len(all_magnet) != 0:
			for magnet in all_magnet:
				i = i + 1
				if i < max_num:
					magnet = re.match(r'"(.*)"',magnet).group(1)
					magnetlist.append(magnet)
			return magnetlist



if __name__ == '__main__':
	max_num=5
	fh_name = argv[1]
	print get_cl(fh_name,max_num)
	