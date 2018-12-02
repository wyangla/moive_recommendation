# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
from entities import Scorer


# operations on each posting unit
class Search_tag():
    
    def __init__(self):
        self.contriScoreCounter = None      # for collecting the contribution scores from each posting units
        self.queryInfo = None               # dictionary, tag and corresponding tf in query
        self.scorer = Scorer()
        
        
    def set_param(self, param):
        self.contriScoreCounter = param[0]
        self.queryInfo = param[1]


    def conduct(self, pUnit):
        self.contriScoreCounter[pUnit.docId] += self.scorer.cal_score(pUnit)
    
    
    