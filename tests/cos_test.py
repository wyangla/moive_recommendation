# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''

import os
os.sys.path.append('..')

from inv_index import Index
from data_structure import Post_unit,Doc, Tag
from probes import Index_probe
from entities import Cos



index = Index()

def prepare_index():
    
    pu1 = Post_unit.deflatten('a -1 -1 -1 {"tf":3} 1 1')
    index.add_post_unit(pu1)
    
    # N == 3
    doc1 = Doc()
    index.docInfo = {1: doc1, 2: Doc(), 3: Doc()}
    
    # doc1 doc length == 5
    doc1.pUnitIds = range(5)
    
    # df = 1
    tag = Tag()
    tag.pUnitIds = list(range(1))
    index.lexicon['a'] = tag
    
    

def test_cos():
    # tf == 3
    pu1 = Post_unit.deflatten('a -1 -1 -1 {"tf":3} 1 1')
    
    cos = Cos()
    print(cos.cal_score(pu1))
    assert(cos.cal_score(pu1) == 0.9509775004326937)


if __name__ == '__main__':
    prepare_index()
    test_cos()