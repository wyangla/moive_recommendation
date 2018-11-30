# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''

import json



class Tag():
    
    def __init__(self, text = ''):
        self.text = text
        self.starterPUnitId = -1    # point to the first posting unit
        self.docCount = 0           # total count of the movie contain this tag
        self.tProp = {}             # currently contain 'maxScore' key
        
        
    def flatten(self):
        # tag text, starterPUnitId, docCount, docPropJson
        flatUnit = "%s %s %s %s"%(self.text, self.starterPUnitId, self.docCount, json.dumps(self.docProp))
        return flatUnit
    
    
    @classmethod
    def deflatten(cls, flatTag):
        tag = cls()
        unitFields = flatTag.split(" ")
        
        tag.text = unitFields[0]
        tag.starterPUnitId = int(unitFields[1])
        tag.docCount = int(unitFields[2])
        tag.docProp = json.loads(unitFields[3])
        
        return tag
    
    
    
if __name__ == '__main__':
    tag = Tag.deflatten('a -1 10 {"maxScore":1}')
    print(tag.__dict__)
    print(tag.flatten())