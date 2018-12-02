# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''
from data_structure import Tag, Post_unit, Doc
from logger import Logger
import global_settings as gs
from global_settings import postingsPath
import os
from utils import decrators
import json
import numpy as np



@decrators.singleton
class Index():
    def __init__(self, logger = None):
        self.lg = logger or Logger.get_logger('Index')
        self.currentPUnitId = 0     # the latest posting unit id
        self.lexicon = {}           # {tagText: tag}
        self.posting = {}           # {pUnitId: pUnit}
        self.docInfo = {}           # {docId: doc}, here is the movie info
        self.queryPool = {}         # {qId: query}, for temporarily store the queries
        
    
    def _get_currentPUnitId(self):
        currentId = self.currentPUnitId
        self.currentPUnitId += 1
        return currentId
    
    
    # the input posting unit does not contain the linking information yet
    # only contains the information extract from the raw dataset
    def add_post_unit(self, pUnit = None):
        pUnit.currentId = self._get_currentPUnitId()
        
        # if pUnit.currentId % 20000 == 0:
        #     self.lg.info('added %d units'%pUnit.currentId)
        
        if not pUnit.tagText in self.lexicon:
            tag = Tag(pUnit.tagText)
            self.lexicon[tag.text] = tag
        else:
            tag = self.lexicon[pUnit.tagText]
            
        # TODO: the tProp is going to be operated by infoManager
        
        pUnitIds = tag.pUnitIds     # the posting list of one tag
        
        if len(pUnitIds) != 0:
            # link the posting units
            previousId = pUnitIds[-1]
            previousUnit = self.posting.get(previousId)
            previousUnit.link_to_next(pUnit)
            pUnit.link_to_previous(previousUnit)
            
        pUnitIds.append(pUnit.currentId)
        
        self.posting[pUnit.currentId] = pUnit
        
        
    def add_doc_info(self, doc):
        self.docInfo[doc.docId] = doc
        
        
    def add_query(self, query):
        while True:
            query.qId = np.random.random(1000000)
            if query.qId not in self.queryPool:
                self.queryPool[query.qId] = query
                break
            
        return query.qId
        
        
    def remove_query(self, qId):
        try:
            self.queryPool.pop(qId)
        except Exception as e:
            self.lg.warn(e)
        
        
    def _persist_lexicon(self):
        self.lg.info('persist lexicon')
        lexiconPath = gs.lexiconPath
        with open(lexiconPath, 'w', encoding = 'utf-8') as f:
            for tagText in self.lexicon:
                tag = self.lexicon[tagText]
                f.write(tag.flatten() + '\n')
    
    
    def _persist_postings(self):
        self.lg.info('persist posting')
        postingsPath = gs.postingsPath
        for tagText in self.lexicon:
            tag = self.lexicon[tagText]
            
            # create the path of posting file
            tagPostingPath = os.path.join(postingsPath, tagText)
            if not os.path.exists(tagPostingPath):
                os.makedirs(tagPostingPath)
            postingFilePath = os.path.join(tagPostingPath, 'posting')
            
            with open(postingFilePath, 'w', encoding = 'utf-8') as f:
                for pId in tag.pUnitIds:
                    pUnit = self.posting[pId]
                    f.write(pUnit.flatten() + '\n')
                    
    
    def _persist_last_pUnitId(self):
        self.lg.info('persist last post unit ID')
        lastPUnitIdPath = gs.lastPUnitIdPath
        with open(lastPUnitIdPath, 'w', encoding = 'utf-8') as f:
            f.write(str(self.currentPUnitId))
    
    
    def _persist_docInfo(self):
        self.lg.info('persist doc info')
        docInfoPath = gs.docInfoPath
        with open(docInfoPath, 'w', encoding = 'utf-8') as f:
            for docId in self.docInfo:
                doc = self.docInfo[docId]
                f.write(doc.flatten() + '\n')
    
    
    def persist_index(self):
        self._persist_last_pUnitId()
        self._persist_lexicon()
        self._persist_postings()
        self._persist_docInfo()
        
        
    def _load_lexicon(self):
        self.lg.info('load lexicon')
        with open(gs.lexiconPath, 'r', encoding = 'utf-8') as f:
            for flatTag in f.readlines():
                tag = Tag.deflatten(flatTag.strip())
                self.lexicon[tag.text] = tag
    
    
    # directly load the persisted posting files
    # does not operate the posting unit ids
    def _load_postings(self):
        self.lg.info('load posting units')
        for tagText in self.lexicon:
            tagPostingPath = os.path.join(postingsPath, tagText)
            postingFilePath = os.path.join(tagPostingPath, 'posting')
            with open(postingFilePath, 'r', encoding = 'utf-8') as f:
                for flatPUnit in f.readlines():
                    pUnit = Post_unit.deflatten(flatPUnit.strip())
                    self.posting[pUnit.currentId] = pUnit
                    
                    # link the list
                    previousUnit = self.posting.get(pUnit.previousId)
                    if previousUnit != None:
                        previousUnit.link_to_next(pUnit)
                        pUnit.link_to_previous(previousUnit)
                        
    
    
    def _load_last_pUnitId(self):
        self.lg.info('load last posting unit id')   # the loaded one will be used directly
        with open(gs.lastPUnitIdPath, 'r') as f:
            self.currentPUnitId = int(f.read().strip())
            
        
    def _load_docInfo(self):
        self.lg.info('load doc info')
        with open(gs.docInfoPath, 'r') as f:
            for flatDoc in f.readlines():
                doc = Doc.deflatten(flatDoc)
                self.docInfo[doc.docId] = doc
    
    
    def load_index(self):
        self._load_last_pUnitId()
        self._load_lexicon()
        self._load_postings()
        self._load_docInfo()
    
    
    def clear_index(self):
        self.currentPUnitId = 0
        self.lexicon = {}
        self.posting = {}
        self.docInfo = {}
    
    