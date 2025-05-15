# -*- coding: utf-8 -*-
"""
Created on Thu May 15 02:18:16 2025

@author: hp
"""
from itertools import combinations
from oops_concepts import item_detail
import pandas as pd

item_list=[]
df = pd.read_excel(r"C:\Users\hp\Downloads\knapsack.xlsx")
for index,row in df.iterrows():
    item = item_detail(row["itemname"],row["itemweight"],row["itemvalue"],row["S.no"])
    item_list.append(item)
 
'''    
items_dict={}    
for i in item_list:
    items_dict[i.identity]=i
 '''   
val= pd.read_excel(r"C:\Users\hp\Downloads\knapsack.xlsx",sheet_name="Sheet2",header=None)   
z=val.iloc[0,1]

allcombination=[]
for j in range(1,len(item_list)+1):
    for combination in combinations(item_list,j):
      allcombination.append(combination)
      
eligiblecombination=[]      
for k in allcombination:
    total_weight=0
    for l in k:
        w = l.itemweight
        total_weight+=w
    if total_weight<=z:
       eligiblecombination.append(k)
       
maxval = 0
for m in eligiblecombination:
       total_value=0
       for n in m:
         v = n.itemvalue
         total_value+=v
       if (total_value>maxval):
         maxval = total_value
         bestcombination=m
    
bestcombinationitems=[]        
for name in bestcombination:
    t=name.itemname
    bestcombinationitems.append(t)
'''
bestitemweight=0
for c in bestcombinationitems:
     x = val 
     bestitemweight+=x
  '''   
print(maxval)
print(bestcombinationitems)
#print(bestitemweight)      
