# -*- coding:utf-8 -*-
'''
Created on 1 Dec 2018

@author: wyan2
'''
import numpy as np



def task_spliter(targetList, workerNum = 3):
    workloads = []
    workload = []
    workloadSize = np.ceil(len(targetList) / workerNum)
    
    for target in targetList:
        workload.append(target)
        
        # once the size of workload reach the 
        if len(workload) >= workloadSize:
            workloads.append(workload)
            workload = []
            
    # collect the rest targets
    if len(workload) != 0:
        workloads.append(workload)
        
    return workloads



if __name__ == '__main__':
    print(task_spliter([1, 2, 3, 4, 5]))
    
    
            
            
            
            