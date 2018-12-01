# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''
import os



serving_port = 11111    # the porting that inverted index is serving at


'''basic path'''
datasetPath = r'./dataset'
persistancePath = r'./persistance'

lexiconPath = os.path.join(persistancePath, 'lexicon')
postingsPath = os.path.join(persistancePath, 'postings')
lastPUnitIdPath = os.path.join(persistancePath, 'lastPUnitId')
docInfoPath = os.path.join(persistancePath, 'docInfo')      # information of each movie


'''multi-threading configs'''
workerNum = 3




