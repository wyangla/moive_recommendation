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



class Advanced_operations():
    
    def __init__(self):
        self.idx = Index()
        self.snr = Scanner()

    
    # docId -> tagList -> search
    def search(self, docId):
        tagList = []
        scoreCounter = Counter()
        
        doc = self.idx.docInfo.get(docId)
        if not type(doc) == type(None):
            for pUnitId in doc.pUnitIds:
                tagList.append(self.idx.posting[pUnitId].tagText)
            
            self.snr.scan(tagList, Search_tag, scoreCounter)
            
        return scoreCounter
    
    
    