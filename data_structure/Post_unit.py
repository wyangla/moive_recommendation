# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''

'''
Modified from my previous work in toyEngine_operator
'''

import json



class Post_unit():
    
    def __init__(self, tagText = 'a', currentId = -1, uProp = None, docId = 0, status = 1):
        self.tagText = tagText
        self.currentId = currentId
        
        self.nextId = -1
        self.nextUnit = None
            
        self.previousId = -1
        self.previousUnit = None

        self.uProp = uProp or {}
        self.docId = docId
        self.status = status


    def flatten(self):
        # tagText, currentId, nextId, previousId, uPropJson, moiveId, status            
        flatUnit = "%s %s %s %s %s %s %s"%(self.tagText, self.currentId, self.nextId, self.previousId, json.dumps(self.uProp), self.docId, self.status)
        flatUnit = flatUnit.replace(": ", ":")
        flatUnit = flatUnit.replace(", ", ",")
        return flatUnit
    
    
    @classmethod
    def deflatten(cls, flatUnit):
        pUnit = cls()
        unitFields = flatUnit.split(" ")
        
        pUnit.tagText = unitFields[0]
        pUnit.currentId = int(unitFields[1])
        pUnit.nextId = int(unitFields[2])
        pUnit.previousId = int(unitFields[3])
        pUnit.uProp = json.loads(unitFields[4])
        pUnit.docId = int(unitFields[5])
        pUnit.status = int(unitFields[6])
        
        return pUnit
    
    
    def link_to_next(self, nextUnit):
        if type(nextUnit) != type(None):
            self.nextUnit = nextUnit
            self.nextId = nextUnit.currentId
    
    
    def link_to_previous(self, previousUnit):
        if type(previousUnit) != type(None):
            self.previousUnit = previousUnit
            self.previousId = previousUnit.currentId
            
        
        
if __name__ == '__main__':    
    pUnit = Post_unit.deflatten('a -1 -1 -1 {"gen_score":1} 100000 1')
    print(pUnit.__dict__)
    print(pUnit.flatten())
        
        
        
        