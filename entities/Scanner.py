# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''
from utils.decrators import singleton
from inv_index import Index



@singleton
class scanner():
    
    def __init__(self):
        self.idx = Index()
    
    
    # iterate over the posting list and apply operations on the units
    def _iterate_over_posting_list(self, currentUnit, operation):
        operation(currentUnit)
        self._iterate_over_posting_list(currentUnit.nextUnit, operation)
    
    
    def scan_tag(self, tag, operation):
        pUnitIds = self.idx.lexicon[tag]
        firstUnit = self.posting[pUnitIds[0]]
        self._iterate_over_posting_list(firstUnit, operation)
        
    
    # DAAT
    def scan(self, tagList):
        workLoads = []
        for tag in tagList:
            pass
    
    
    
    
    
    
        