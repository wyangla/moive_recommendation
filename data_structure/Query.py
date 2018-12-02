# -*- coding:utf-8 -*-
'''
Created on 2 Dec 2018

@author: wyan2
'''



class Query():
    
    def __init__(self):
        self.qId = -1
        self.tagTf = {}     # {tagText: tf}
        self.tagScore = {}  # {tagText: score}, e.g. tfidf
        self.qProp = {}     # not used yet