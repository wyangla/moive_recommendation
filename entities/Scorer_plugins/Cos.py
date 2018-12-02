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
        
        # docLen = self.idx.docInfo[pUnit.docId].basicInfo['tagNum']

        # if the vector length is not calculated
        if type(self.idx.docInfo[pUnit.docId].basicInfo.get('vecLen')) == type(None):
            squareSum = 0
            for pUnitId in self.idx.lexicon[pUnit.tagText].pUnitIds:
                squareSum += self.idx.posting[pUnitId].uProp['tf'] ** 2    
            vecLen = np.sqrt(squareSum)
            
            self.idx.docInfo[pUnit.docId].basicInfo['vecLen'] = vecLen
        else:
            vecLen = self.idx.docInfo[pUnit.docId].basicInfo['vecLen']
            
                
        normalizedTfidf = tfidf / vecLen
        return normalizedTfidf
        
        
        
        
        
        
        
        