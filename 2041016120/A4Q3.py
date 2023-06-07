#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:34:59 2023

@author: Adarsh Patel 

A4Q3
"""

from dataclasses import dataclass

@dataclass
class Roll_No:
    name:str
    branch:str
    year_of_admission:int

roll_nos = []    
r1 = Roll_No("Adarsh", "CSE", 2021)
roll_nos.append(r1)
r1 = Roll_No("Nishikant", "CSE", 2021)
roll_nos.append(r1)
r1 = Roll_No("Ravi", "CSE", 2021)
roll_nos.append(r1)
for r in roll_nos:
    print(r)
