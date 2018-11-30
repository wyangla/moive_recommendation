# -*- coding:utf-8 -*-
'''
Created on 30 Oct 2018

@author: wyan2
'''


# ref: https://www.cnblogs.com/guomeina/p/7687012.html
def singleton(cls):
    insPool = {}
    def get_instance(*args, **kw):
        if cls not in insPool:
            insPool[cls] = cls(*args, **kw)
        return insPool[cls]
    return get_instance