# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
import json



class Doc():
    
    def __init__(self):
        self.docId = -1
        self.basicInfo = {}     # collecting the basic information from the raw data
        self.pUnitIds = []      # maps to the corresponding posting units
    
    
    def flatten(self):
        flatDoc = '%s %s %s'%(self.docId, json.dumps(self.basicInfo), json.dumps(self.pUnitIds))
        flatDoc = flatDoc.replace(": ", ":")
        flatDoc = flatDoc.replace(", ", ",")
        return flatDoc
    
        
    @classmethod
    def deflatten(self, flatDoc):
        doc = Doc()
        docFields = flatDoc.split(" ")
        
        doc.docId = docFields[0]
        doc.basicInfo = json.loads(docFields[1])
        doc.pUnitIds = json.loads(docFields[2])
        
        return doc
        
        
        
if __name__ == '__main__':
    flatDoc = '5 {"title":"test","genre":"test"} [1,2]'
    doc = Doc.deflatten(flatDoc)
    print(doc.__dict__)
    print(doc.flatten())
    
    
        