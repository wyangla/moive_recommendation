# -*- coding:utf-8 -*-
'''
Created on 2 Dec 2018

@author: wyan2
'''



class Query():
    
    def __init__(self):
        self.qId = -1
        self.tagTf = {}     # {tagText: tf}
        self.qProp = {}     # store the calculated tag contribute scores, e.g. tfidf