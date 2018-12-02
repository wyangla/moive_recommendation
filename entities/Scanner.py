# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''

import os, sys
os.sys.path.append('..')
sys.setrecursionlimit(5000)     # the largest recursion times

from inv_index import Index
from logger import Logger
# from utils import general
# import global_settings as gs



class Scanner():
    
    def __init__(self, logger = None):
        self.lg = logger or Logger.get_logger('Scanner')
        self.idx = Index()
    
    
    # iterate over the posting list and apply operations on the units
    def _iterate_over_posting_list(self, currentUnit, operationConductFunc): # 'entities.Test'
        operationConductFunc(currentUnit)
        nextUnit = currentUnit.nextUnit
        if type(nextUnit) != type(None):
            self._iterate_over_posting_list(currentUnit.nextUnit, operationConductFunc)
    
    
    # TAAT
    def scan(self, tagList, operationCls, operationParam, query = None):
        
        operation = operationCls()
        operation.set_query(query)              # pass the query into operation
        operation.set_param(operationParam)     # set parameter into operation
        operationConductFunc = operation.conduct
        
        for tagText in tagList:
            tag = self.idx.lexicon.get(tagText)
            
            if type(tag) != type(None):         # skip the non-existing tag
                pUnitIds = tag.pUnitIds
                currentUnit = self.idx.posting[pUnitIds[0]]
                self._iterate_over_posting_list(currentUnit, operationConductFunc)

        
    
    
    
    
        