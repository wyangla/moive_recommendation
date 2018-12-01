# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
from inv_index import Index
from entities import Scanner
from entities import Search_tag
from collections import Counter
import json



class Adcanced_operations():
    
    def __init__(self):
        self.idx = Index()
        self.snr = Scanner()

    
    # docId -> tagList -> search
    def search(self, docId):
        retMsg = ''     # the returned message
        tagList = []
        scoreCounter = Counter()
        
        doc = self.idx.docInfo.get(docId)
        if type(doc) == type(None):
            retMsg = 'movie is not existing'
        else:
            for pUnitId in doc.pUnitIds:
                tagList.append(self.idx.posting[pUnitId].tagText)
            
            self.snr.scan(tagList, Search_tag, scoreCounter)
            
            
        return retMsg
    
    
    