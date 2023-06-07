#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:09:18 2023

@author: Adarsh Patel 
A1Q7
"""

import requests
import csv
import random
import math
from typing import NamedTuple,List,Tuple,Dict
from sklearn.model_selection import train_test_split
from collections import defaultdict,Counter
Vector=List[float]

class LabeledPoint(NamedTuple):
    point:Vector
    label:str

def majority_vote(labels):
    vote_counts=Counter(labels)
    winner,winner_count=vote_counts.most_common(1)[0]
    num_winners=len([count for count in vote_counts.values() if count==winner_count])
    if num_winners==1:
        return winner
    else:import tqdm
import random
import math
import matplotlib.pyplot as plt
def dot(v, w):
assert len(v) == len(w)
return sum(v_i * w_i for v_i, w_i in zip(v, w))
def sum_of_squares(v):
return dot(v, v)
def magnitude(v):
return math.sqrt(sum_of_squares(v))
def subtract(v,w):
assert len(v)==len(w)
return [v_i-w_i for v_i,w_i in zip(v, w)]
def distance(v,w):
return magnitude(subtract(v, w))
def random_point(dim):
return [random.random() for _ in range(dim)]
def random_distance(dim,num_pairs):
return [distance(random_point(dim),random_point(dim)) for _ in range(num_pairs)]
def main():
dimensions=range(1,101)
avg_distances,min_distances=[],[]
random.seed(0)
for dim in tqdm.tqdm(dimensions,desc='Curse Of Dimensionality'):
distances=random_distance(dim,10000)
avg_distances.append(sum(distances)/10000)
min_distances.append(min(distances))
min_avg_ratio=[min_dist/avg_dist for min_dist,avg_dist in zip(min_distances,avg_distances)]
plt.xlabel('No. Of Dimensions')
plt.ylabel('Distance')
plt.plot(dimensions,avg_distances,label='Average Distance')
plt.plot(dimensions,min_distances,label='Minimum Distance')
plt.legend()
plt.show()
min_avg_ratio=[min_dist/avg_dist for min_dist,avg_dist in zip(min_distances,avg_distances)]
plt.xlabel('No. Of Dimensions')
plt.ylabel('Distance')
plt.plot(dimensions,min_avg_ratio,label='Minimum Distance/Average Distance')
plt.legend()
plt.show()
if name ==' main ':
main()
        return majority_vote(labels[:-1])
    
def knn_classify(k,labeled_points,new_points):
    by_distance=sorted(labeled_points,key=lambda lp:distance(lp.point,new_points))
    k_nearest_labels=[lp.label for lp in by_distance[:k]]
    return majority_vote(k_nearest_labels)


def dot(v, w):
    assert len(v) == len(w)
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
def sum_of_squares(v):
    return dot(v, v)
def magnitude(v):
    return math.sqrt(sum_of_squares(v))
def subtract(v,w):
    assert len(v)==len(w)
    return [v_i-w_i for v_i,w_i in zip(v, w)]
def distance(v,w):
    return magnitude(subtract(v, w))
def parse_iris_row(row:List[str]):
    measurements=[float(value) for value in row[:-1]]
    label=row[-1].split("-")[-1]
    return LabeledPoint(measurements,label)


with open('iris.data') as f:
    reader=csv.reader(f)
    iris_data=[parse_iris_row(row) for row in reader if row!=[]]
    random.seed(12)
    iris_train,iris_test=train_test_split(iris_data,test_size=0.30)
    assert len(iris_train)==0.7*150
    assert len(iris_test)==0.3*150
    confusion_matrix:Dict[Tuple[str,str],int]=defaultdict(int)
    num_correct=0
    for iris in iris_test:
        predict=knn_classify(5,iris_train,iris.point)
        actual=iris.label
        if predict==actual:
            num_correct+=1
        confusion_matrix[(predict,actual)]+=1
    pct_correct=num_correct/len(iris_test)
    print(pct_correct,confusion_matrix)