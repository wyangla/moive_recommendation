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
        
        
    def _cal_unit_tfidf(self, pUnit):
        df = len(self.idx.lexicon[pUnit.tagText].pUnitIds)      # document frequency
        N = len(self.idx.docInfo)                               # total document amount
        tf = pUnit.uProp.get('tf')                              # tag frequency in document
        uTfidf = tf * np.log2(N / df)                       
        pUnit.uProp['tfidf'] = uTfidf                           # store the calculated tfidf
        return uTfidf
        
        
    # calculate the vec len of doc
    def _cal_vec_len(self, pUnit):
        # if the vector length of a doc is not calculated
        doc = self.idx.docInfo[pUnit.docId]
        if type(doc.basicInfo.get('vecLen')) == type(None):
            squareSum = 0
            for pUnitId in doc.pUnitIds:
                pUnit = self.idx.posting[pUnitId]
                
                if type(pUnit.uProp.get('tfidf')) == type(None):    # the uTfidf is not calculated yet
                    uTfidf = self._cal_unit_tfidf(pUnit)
                else:
                    uTfidf = pUnit.uProp['tfidf']       
                        
                squareSum += uTfidf ** 2
            vecLen = np.sqrt(squareSum) 
            
            self.idx.docInfo[pUnit.docId].basicInfo['vecLen'] = vecLen
        else:
            vecLen = self.idx.docInfo[pUnit.docId].basicInfo['vecLen']
        
        return vecLen
        

    # here in fact only computes the tfidf, not cos, cos need all the tfidf value 
    def cal_score(self, pUnit, query):
        
        # get tfidf value contributed by a posting unit
        if type(pUnit.uProp.get('tfidf')) == type(None):
            uTfidf = self._cal_unit_tfidf(pUnit)
        else:
            uTfidf = pUnit.uProp['tfidf']

        # calculate tfidf of the tagText in the query
        if type(query.tagScore.get(pUnit.tagText)) == type(None):
            df = len(self.idx.lexicon[pUnit.tagText].pUnitIds)
            N = len(self.idx.docInfo)
            qTf = query.tagTf[pUnit.tagText]
            qTfidf = qTf * np.log2(N / df)
            query.tagScore[pUnit.tagText] = qTfidf
        else:
            qTfidf = query.tagScore[pUnit.tagText]

        # docLen = self.idx.docInfo[pUnit.docId].basicInfo['tagNum']
            
        vecLen = self._cal_vec_len(pUnit)
        normalizedTfidf = qTfidf * uTfidf / vecLen
        
        return normalizedTfidf
        
        
        
        
        
        
        
        