# -*- coding:utf-8 -*-
'''
Created on 2 Dec 2018

@author: wyan2
'''

'''
for conduct searching in console
'''

import sys
import urllib.request
import global_settings as gs


def main():
    docId = int(sys.argv[1])
    req = urllib.request.Request('http://127.0.0.1:%d/search?movieId=%d'%(gs.servingPort, docId))
    opener = urllib.request.build_opener()
    response = opener.open(req)
    displayMsg = response.read()
    print(displayMsg)



if __name__ == '__main__':
    main()

