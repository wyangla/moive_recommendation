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
    
    def __init__(self, tag = 'a', currentId = -1, nextId = -1, previousId = -1, uProp = {}, moiveId = 100, status = 1):
        self.tag = tag
        self.currentId = currentId
        self.nextId = nextId
        self.previousId = previousId
        self.uProp = uProp
        self.moiveId = moiveId
        self.status = status


    def flatten(self):
        # currentId, nextId, previousId, uPropJson, moiveId, status
        flatUnit = "%s %s %s %s %s %s %s"%(self.tag, self.currentId, self.nextId, self.previousId, json.dumps(self.uProp), self.moiveId, self.status)
        return flatUnit
    
    
    @classmethod
    def deflatten(cls, flatUnit):
        pUnit = cls()
        unitFields = flatUnit.split(" ")
        
        pUnit.tag = unitFields[0]
        pUnit.currentId = int(unitFields[1])
        pUnit.nextId = int(unitFields[2])
        pUnit.previousId = int(unitFields[3])
        pUnit.uProp = json.loads(unitFields[4])
        pUnit.moiveId = unitFields[5]
        pUnit.status = int(unitFields[6])
        
        return pUnit
        
        
        
if __name__ == '__main__':    
    pUnit = Post_unit.deflatten('1 -1 -1 -1 {"tf":1} 100000 1')
    print(pUnit.__dict__)
    print(pUnit.flatten())
        
        
        
        