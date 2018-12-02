# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
import os
os.sys.path.append('..')


from inv_index import Index
from entities import Scanner
from entities import Search_tag
from collections import Counter
import json
import global_settings as gs
from copy import deepcopy



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
    
    
    # transfer the searching result into readable information
    def display_search(self, docId):
        displayMsgList = []
        scoreCounter = self.search(docId)
        topKRecords = scoreCounter.most_common(gs.topK)
        
        for record in topKRecords:
            docId = record[0]
            score = record[1]
            basicInfo = self.idx.docInfo.get(docId).basicInfo
            
            # docId, ranking_score, title, genre, tagNum
            displayMsgList.append('%d\t%f\t%-50s\t%-30s\t%d\n'%(docId, score, basicInfo['title'], basicInfo['genre'], basicInfo['tagNum']))
    
        displayMsg = ''.join(displayMsgList)
        return displayMsg
    