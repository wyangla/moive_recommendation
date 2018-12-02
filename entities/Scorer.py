# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
import os
os.sys.path.append('..')

import global_settings as gs



class Scorer():
    
    def __init__(self):
        pass
    
    
    def cal_score(self, pUnit, query = None):
        scoringModelModule = __import__(gs.scorerPluginPath + gs.scoringModel)
        scoringModel = getattr(scoringModelModule, gs.scoringModel)
        contriScore = scoringModel().cal_score(pUnit, query)
        return contriScore
    
    
    
if __name__ == '__main__':
    Scorer().cal_score()
    
    
    