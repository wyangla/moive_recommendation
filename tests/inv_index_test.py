# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''
import os
os.sys.path.append('..')

from inv_index import Index
from data_structure import Post_unit
from probes import Index_probe


index = Index()

def prepare_index():
    pu1 = Post_unit.deflatten('a -1 -1 -1 {"gen_score":1} 1 1')
    pu2 = Post_unit.deflatten('b -1 -1 -1 {"gen_score":1} 2 1')
    pu3 = Post_unit.deflatten('a -1 -1 -1 {"gen_score":1} 5 1')
    pu4 = Post_unit.deflatten('a -1 -1 -1 {"gen_score":1} 6 1')
    
    
    '''test adding posting unti'''
    index.add_post_unit(pu1)
    index.add_post_unit(pu2)
    index.add_post_unit(pu3)
    index.add_post_unit(pu4)
    
    Index_probe().display()
    
    
def test_persisting():
    '''test persisting'''
    os.chdir('..')
    index.persist_index()
        
    
def test_loading():
    '''test loading'''
    os.chdir('..')
    index.load_index()
    
    Index_probe().display()
    
    
    
if __name__ == '__main__':
    test_loading()
    
    
