# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
import os
os.sys.path.append('..')

from data_structure import Query
from inv_index import Index
from entities import Scanner
from entities import Search_tag
from collections import Counter
import json
import global_settings as gs
from copy import deepcopy
import traceback



class Advanced_operations():
    
    def __init__(self):
        self.idx = Index()
        self.snr = Scanner()

    
    # docId -> tagList -> search
    def search(self, docId):
        query = Query()
        scoreCounter = Counter()
        
        doc = self.idx.docInfo.get(docId)
        if not type(doc) == type(None):             # if the searched movie is existing
            for pUnitId in doc.pUnitIds:
                pUnit = self.idx.posting[pUnitId]
                query.tagTf[pUnit.tagText] = pUnit.uProp['tf'] 
            
                qId = self.idx.add_query()          # add the query to index, for the usage during scanning
                try:
                    tagList = list(query.tagTf.keys())
                    self.snr.scan(tagList, Search_tag, scoreCounter)
                except Exception as e:
                    self.lg.warn(traceback.format_exc())
                    
                self.idx.remove_query(qId)          # remove the query from index, after searching
            
        return scoreCounter
    
    
    # transfer the searching result into readable information
    def display_search(self, docId):
        displayMsgList = []
        scoreCounter = self.search(docId)
        
        if len(scoreCounter) > 0:
            # scoreCounter.pop(docId)
            topKRecords = scoreCounter.most_common(gs.topK)
            
            # head line
            displayMsgList.append('%s\t%-20s\t%-50s\t%-30s\t%s\n'%('docId', 'rankingScore', 'title', 'genre', 'tagNum'))
            
            # info of searched movie
            # basicInfo = self.idx.docInfo.get(docId).basicInfo
            # displayMsgList.append('%d\t%-20s\t%-50s\t%-30s\t%d\n\n'%(docId, '-', basicInfo['title'], basicInfo['genre'], basicInfo['tagNum']))
            
            
            # info of the recommendations
            for record in topKRecords:
                docId = record[0]
                score = record[1]
                basicInfo = self.idx.docInfo.get(docId).basicInfo
                
                # docId, ranking_score, title, genre, tagNum
                displayMsgList.append('%d\t%-20f\t%-50s\t%-30s\t%d\n'%(docId, score, basicInfo['title'], basicInfo['genre'], basicInfo['tagNum']))
        
            displayMsg = ''.join(displayMsgList)
            
        else:
            displayMsg = 'Searched movie is not existing.'
        return displayMsg
    