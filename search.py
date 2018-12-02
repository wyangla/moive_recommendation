# -*- coding:utf-8 -*-
'''
Created on 2 Dec 2018

@author: wyan2
'''

'''
for conduct searching in console
'''

from inv_index import Advanced_operations

adOps = Advanced_operations()
docId = int(input('please input the moviedId')[1])
adOps.search(docId)


