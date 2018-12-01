# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
from entities import OperationOnUnit 



class Test(OperationOnUnit):
    def __init__(self):
        pass


    def set_param(self):
        pass


    def conduct(self, pUnit):
        print('conduct operation on post unit')
    
    
    
if __name__ == '__main__':
    t = Test()
    
    
    