# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
from entities import Scorer



# operations on each posting unit
# different from normal search, as having qtf
class Search_tag():
    
    def __init__(self):
        self.contriScoreCounter = None      # for collecting the contribution scores from each posting units
        self.query = None
        self.scorer = Scorer()
        

    def set_query(self, query):
        self.query = query

        
    def set_param(self, contriScoreCounter):
        self.contriScoreCounter = contriScoreCounter


    def conduct(self, pUnit):
        self.contriScoreCounter[pUnit.docId] += self.scorer.cal_score(pUnit, self.query)
    
    
    