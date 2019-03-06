# -*- coding: utf-8 -*-
"""
@author: Jeremy
"""

# -*- coding: utf-8 -*-
import numpy as np

Category = {1:'-macrobiotic fds/tofu/japanese',
2:'-refrigerated misc.',
3:'-refrigerated soy foods/seitan',
4:'-refrigerated beverages',
5:'-other dairy & alternatives',
6:'-refrigerated cheese & subst.',
7:'-refrigerated misc.',
8:'-refrigerated yogurts/cultures',
9:'-rf bread & baked goods',
10:'-refrigerated soy foods/seitan',
11:'-macrobiotic fds/tofu/japanese',
12:'-refrigerated salsas & dips',
13:'-yogurt & kefir',
14:'-rf juices & functional bev'}

ref = {'1':0.35,'2':0.35,'3':0.42,'4':0.28,'5':0.38,'6':0.37,'7':0.35,'8':0.27,'9':0.33,'10':0.42,'11':0.35,'12':0.41,'13':0.36,'14':0.36}

for key in Category:
    print(key," - ", Category[key])
    
Cost = float(input("Please enter cost: "))

Department = input("Please enter category name: ")

Price = Cost/(ref[Department] -1)*-1

Price_round = np.round(Price,2)

print("Price at margin is:", Price_round)