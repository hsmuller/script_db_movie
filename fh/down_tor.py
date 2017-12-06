# -*- coding:utf-8 -*-

import requests
from sys import argv
from get_fh import *
from get_cl import *
from cl2zz import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def ny2cl(ny_name):
	search_result = {}
	fh_info = get_fh(ny_name)
 	for (fh_name,fh_time) in fh_info.items():
 		magnetlist = get_cl(fh_name,2)
 		for magnet in magnetlist:
 			search_result[fh_name] = magnet
 	return search_result

def download_zz(fh_name,magnet):
	zz_url = cl2zz(magnet)
	r = requests.get(zz_url)
	if r.status_code == 200:
		with open('zz/' + fh_name + '.torrent','wb') as code :
			code.write(r.content)
	else:
		pass

if __name__ == '__main__':
 	ny_name = argv[1]
 	search_result = ny2cl(ny_name)
 	for (fh_name,magnet) in search_result.items():
 		download_zz(fh_name,magnet)
 		print "done"
 	raw_input()
