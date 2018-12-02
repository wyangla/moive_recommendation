# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
import os
os.chdir('..')

from inv_index import Index, Advanced_operations



def test__search():
    idx = Index()
    idx.load_index()
    adOps = Advanced_operations()
    print(adOps.search(541).most_common(10))
    
    
def test_display_search():
    docId = 11
    idx = Index()
    idx.load_index()
    adOps = Advanced_operations()
    print(adOps.display_search(docId))
    print()
    print(adOps.search(docId))    



if __name__ == '__main__':
#     test_search()
    test_display_search()
    
    