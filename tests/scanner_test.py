# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
import os
os.chdir('..')

from entities import Scanner
from entities import Test, Search_tag
from inv_index import Index
from collections import Counter


'''
N: 19501

dark_hero: df 24
noir_thriller: df 32

not dividing the queryLen here, but the order is the same
[cos == tf * np.log2(19501 / df) / docLen]

doc 1783: len 4, dark_hero_tf 0, noir_thriller_tf 12, 27.75378145796531
doc 7223: len 8, dark_hero_tf 0, noir_thriller_tf 21, 24.28455877571965
doc 1617: len 72, dark_hero_tf 0, noir_thriller_tf 3, 0.38546918691618487
doc 32587: len 161, dark_hero_tf 2, noir_thriller_tf 0, 0.12007823584182956
doc 541: len 178, dark_hero_tf 1, noir_thriller_tf 1, 0.1062784183778411

'''



def test_scanner():
    idx = Index()
    idx.load_index()
    snr = Scanner()
#     snr.scan(['dark_hero', 'noir_thriller'], Test, 'Test')
    
    scoreCounter = Counter()
    snr.scan(['dark_hero', 'noir_thriller'], Search_tag, scoreCounter)
    print(scoreCounter)
    
    
    
if __name__ == '__main__':
    test_scanner()
    
    