#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:47:21 2023

@author: Adarsh Patel
A4Q5

"""


import csv
from sklearn.model_selection import train_test_split

def loadDataset():
    with open('Advertising.csv') as csvfile:
        csv_reader=csv.reader(csvfile)
        header=[]
        header=next(csv_reader)
        print('Header:',header)
        rows=[]
        for row in csv_reader:
            rows.append(row)
        
        return rows

data_set=loadDataset()
print('No. Of Rows Before Split In A Data Set:',len(data_set))
Advertising_train,Advertising_test=train_test_split(data_set,test_size=0.30)
print('No. Of Rows After Split In A Train Data Set:',len(Advertising_train))
print('No. Of Rows After Split In A Test Data Set:',len(Advertising_test))
