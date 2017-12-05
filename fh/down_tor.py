# -*- coding:utf-8 -*-

from sys import argv
from get_fh import *
from get_cl import *
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


if __name__ == '__main__':
 	ny_name = argv[1]
 	search_result = ny2cl(ny_name)
 	for (fh_name,magnet) in search_result.items():
 		print fh_name
 		print magnet

