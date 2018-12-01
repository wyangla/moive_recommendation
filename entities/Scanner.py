# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''

import os
os.sys.path.append('..')

from inv_index import Index
# from utils import general
# import global_settings as gs



class Scanner():
    
    def __init__(self):
        self.idx = Index()
    
    
    # iterate over the posting list and apply operations on the units
    def _iterate_over_posting_list(self, currentUnit, operationConductFunc): # 'entities.Test'
        operationConductFunc(currentUnit)
        nextUnit = currentUnit.nextUnit
        if type(nextUnit) != type(None):
            self._iterate_over_posting_list(currentUnit.nextUnit, operationConductFunc)
    
    
    # TAAT
    def scan(self, tagList, operationCls, operationParam):
        
        operation = operationCls()
        operation.set_param(operationParam)
        operationConductFunc = operation.conduct
        
        for tagText in tagList:
            tag = self.idx.lexicon.get(tagText)
            
            if type(tag) != type(None):     # skip the non-existing tag
                pUnitIds = tag.pUnitIds
                currentUnit = self.idx.posting[pUnitIds[0]]
                self._iterate_over_posting_list(currentUnit, operationConductFunc)

        
    
    
    
    
        