# -*- coding:utf-8 -*-

import requests
import sys
import json
import re
import sys

def cl2zz(magnet):
#    magnet = "magnet:?xt=urn:btih:2fe3f3dea1e7ef9f0a56abd00ae6e0fafda05f90"
    sub_dict={'"':'%22','#':'%23','&':'%26','(':'%28',')':'%29','+':'%2B',',':'%2C',':':'%3A',';':'%3B','<':'%3C','=':'%3D','?':'%3F','@':'%40','|':'%7C'}
    for (k,v) in sub_dict.items():
        magnet = magnet.replace(k,v)
    magnet = "magnet=" + magnet
    url = "https://tool.acgche.com/magnet2torrent.php?" + magnet
    html = requests.get(url)
    if html.status_code == 200:
        text = html.content
        zz_data = json.loads(text)
        zz_url = zz_data['url']
    else:
        print "error"
        sys.exit()
    return zz_url

def main():
    magnet = "magnet:?xt=urn:btih:CC5F55F06E6AACF19B4DCB8BC6426D4847F30DB6"
    print cl2zz(magnet)
    raw_input()

if __name__ == '__main__':
    main()



