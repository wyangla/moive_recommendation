# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
from entities import Scorer



class Search_tag():
    
    def __init__(self):
        self.contriScoreCounter = None    # for collecting the contribution scores from each posting units
        self.scorer = Scorer()
        
        
    def set_param(self, contriScoreCounter):
        self.contriScoreCounter = contriScoreCounter


    def conduct(self, pUnit):
        self.contriScoreCounter[pUnit.docId] += self.scorer.cal_score(pUnit)
    
    
    