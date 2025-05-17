# -*- coding: utf-8 -*-
"""
Created on Fri May 16 16:40:00 2025

@author: hp
"""

from oops_concepts import item_detail
import pandas as pd


item_list=[]
df = pd.read_excel(r"C:\Users\hp\Downloads\knapsack.xlsx")
for index,row in df.iterrows():
    item = item_detail(row["itemname"],row["itemweight"],row["itemvalue"],row["S.no"])
    item_list.append(item)
    
#defgreedy_solution():
val= pd.read_excel(r"C:\Users\hp\Downloads\knapsack.xlsx",sheet_name="Sheet2",header=None)   
capacity=val.iloc[0,1]

sorted_items = sorted(item_list, key=lambda x: x.itemvalue, reverse=True)

items_in_bag=[] 
remaining_capacity = capacity

total_weight_in_bag=0
total_item_value=0
for i in sorted_items:
    if i.itemweight < remaining_capacity:
        items_in_bag.append(i.itemname)
        remaining_capacity -= i.itemweight
        total_weight_in_bag += i.itemweight
        total_item_value += i.itemvalue
        

print(items_in_bag)
print(remaining_capacity)
print(total_weight_in_bag)
print(total_item_value)
    
# Value per unit weight

     
      
    
    
    
    
    
    
    
    
    




    