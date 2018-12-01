# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
from entities import OperationOnUnit



class Test(OperationOnUnit):
    def __init__(self):
        pass


    def set_param(self, param):
        print('param set: ' + str(param))


    def conduct(self, pUnit):
        print(pUnit.docId)
    
    
    
if __name__ == '__main__':
    t = Test()
    
    
    