# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''
import os
os.sys.path.append('..')

from utils.decrators import singleton
from inv_index import Index
from utils import general
import global_settings as gs



@singleton
class scanner():
    
    def __init__(self):
        self.idx = Index()
    
    
    # iterate over the posting list and apply operations on the units
    def _iterate_over_posting_list(self, currentUnit, operationCls):
        operationCls(currentUnit)
        self._iterate_over_posting_list(currentUnit.nextUnit, operationCls)
    
    
    def scan_tags(self, tagList, operation):
        for tag in tagList:
            pUnitIds = self.idx.lexicon[tag]
            firstUnit = self.posting[pUnitIds[0]]
            self._iterate_over_posting_list(firstUnit, operation)
        
    
    # DAAT
    def scan(self, tagList):
        workloads = general.task_spliter(tagList, gs.workerNum)
        for workload in workloads:
            pass
    
    
    
    
    
        