# -*- coding:utf-8 -*-
'''
Created on 18 Oct 2018

@author: wyan2
'''

'''
Reused from my previous work
'''

# import sys
# sys.path.append('..')
from logging import getLogger, Formatter
from logging import handlers, StreamHandler



class Logger():
    
    @classmethod
    def get_logger(self, name = 'test', logLevel = 'DEBUG', persist = True):
        lg = getLogger(name)
        lg.setLevel(logLevel)
        
        fmt = Formatter('%(asctime)s [%(levelname)s] - %(filename)s:%(lineno)s %(message)s')
        
        if persist:
            fhandler = handlers.RotatingFileHandler('./' + name + '.log', mode = 'a', maxBytes = 1024 * 1024, backupCount = 3)
            fhandler.setFormatter(fmt)
            lg.addHandler(fhandler)
        
        shandler = StreamHandler()
        shandler.setFormatter(fmt)
        lg.addHandler(shandler)
        
        return lg
    
    
    
if __name__ == '__main__':
    lg = Logger.get_logger('test_1')
    lg.info('test logger')
    
    