# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
from abc import ABC, abstractmethod



class OperationOnUnit(ABC):
    
    @abstractmethod
    def set_query(self, query):
        pass
    
    @abstractmethod
    def set_param(self, param):
        pass
    
    @abstractmethod
    def conduct(self, pUnit):
        pass