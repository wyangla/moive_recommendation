# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
import os
os.chdir('..')

from inv_index import Index, Advanced_operations



def test_search():
    idx = Index()
    idx.load_index()
    adOps = Advanced_operations()
    print(adOps.search(541).most_common(10))
    
    

if __name__ == '__main__':
    test_search()