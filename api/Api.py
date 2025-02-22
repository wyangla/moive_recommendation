# -*- coding:utf-8 -*-
'''
Created on 30 Nov 2018

@author: wyan2
'''

'''
Refer to my previous work
'''

from flask import Flask, render_template, request
from inv_index import Index, Advanced_operations
from logger import Logger
import global_settings as gs



logger = Logger.get_logger('movie_recommendation', True)
idx = Index(logger)
adOps = Advanced_operations(logger)


app = Flask(__name__)


@app.route('/search', methods=['POST', 'GET'])
def search():
    movieId = int(request.args['movieId'])
    return str(adOps.search(movieId))


@app.route('/display_search', methods=['POST', 'GET'])
def display_search():
    movieId = int(request.args['movieId'])
    return adOps.display_search(movieId)


def start_serving():
    global idx
    idx.load_index()    # initialise the inverted-index
    app.run(host='127.0.0.1', port = gs.servingPort, threaded=True)



if __name__ == '__main__':
    import os
    os.chdir('..')
    start_serving()
    
    
    
    
    
    