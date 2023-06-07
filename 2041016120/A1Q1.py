#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:53:52 2023

@author: Adarsh Patel
A1Q1
"""
import random
from matplotlib import pyplot as plt

nums=[ random.randrange(1,101) for _ in range(101)]

print('Generated Random Numbers:',nums)
plt.hist(nums,bins=10,color='skyblue',edgecolor='blue')
plt.xlabel('Generated Random Numbers Range 1 to 100 Including')
plt.ylabel('Frequency Count')
plt.title('Generated Random Numbers Range 1 to 100 Including Vs Frequency Count')
plt.show()