# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''

import json



class Tag():
    
    def __init__(self, text = ''):
        self.text = text
        self.pUnitIds = []          # list of posting units of one tag
        self.tProp = {}             # currently contain 'maxScore' key
        
        
    def flatten(self):
        # tag text, pUnitIds, docPropJson
        flatTag = "%s %s %s"%(self.text, json.dumps(self.pUnitIds), json.dumps(self.tProp))
        flatTag = flatTag.replace(": ", ":")
        flatTag = flatTag.replace(", ", ",")
        return flatTag
    
    
    @classmethod
    def deflatten(cls, flatTag):
        tag = cls()
        tagFields = flatTag.split(" ")
        
        tag.text = tagFields[0]
        tag.pUnitIds = json.loads(tagFields[1])
        tag.tProp = json.loads(tagFields[2])
        
        return tag
    
    
    
if __name__ == '__main__':
    tag = Tag.deflatten('a [-1,2,3] {"maxScore":1}')
    print(tag.__dict__)
    print(tag.flatten())