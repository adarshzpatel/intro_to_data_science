#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:29:05 2023

@author: Adarsh patel
A4Q2
"""

from collections import namedtuple

roll_no=namedtuple("Roll_No",["Name","Branch","Year_Of_Admission"])
roll=[]
r1=roll_no('Adarsh','CSE',2021)
roll.append(r1)

r2=roll_no('Nishikant','CSE',2021)
roll.append(r2)

r3=roll_no('Shivam','CSE',2023)
roll.append(r3)

print('Named Tuple: Roll_No')
for r in roll:
    print(r)
