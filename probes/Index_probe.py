# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''
from inv_index import Index




class Index_probe():
    
    def __init__(self):
        self.idx = Index()
        
    
    # show statistic information
    def show(self):
        statisticInfo = {}
        statisticInfo['lexicon size'] = len(self.idx.lexicon)
        statisticInfo['posting size'] = len(self.idx.posting)
        statisticInfo['movieInfo size'] = len(self.idx.docInfo)
        print(statisticInfo)
    
    
    # show detailed information
    def display(self):
        index = self.idx
        
        for text in index.lexicon:
            tag = index.lexicon[text]
            print(text + '\t' + str(tag.pUnitIds))
            
        print(index.posting)
        for pId in index.posting:
            print(index.posting[pId].tagText)
            
        print(index.docInfo)
        
    
    