# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
from inv_index import Index
import numpy as np



class Cos():
    
    def __init__(self):
        self.idx = Index()
        
    
    def cal_score(self, pUnit):
        tf = pUnit.uProp.get('tf')
        df = len(self.idx.lexicon[pUnit.tagText].pUnitIds)
        N = len(self.idx.docInfo)
        tfidf = tf * np.log2(N / df)
        docLen = len(self.idx.docInfo[pUnit.docId].pUnitIds)
        normalizedTfidf = tfidf / docLen
        return normalizedTfidf
        
        
        
        
        
        
        
        