# -*- coding: utf-8 -*-
"""
Created on Sun May 18 14:52:18 2025

@author: hp
"""
from oops_concepts import item_detail
import pandas as pd


item_list=[]
df = pd.read_excel(r"C:\Users\hp\Downloads\knapsack.xlsx")
for index,row in df.iterrows():
    item = item_detail(row["itemname"],row["itemweight"],row["itemvalue"],row["S.no"])
    item_list.append(item)

val= pd.read_excel(r"C:\Users\hp\Downloads\knapsack.xlsx",sheet_name="Sheet2",header=None)   
capacity=val.iloc[0,1]
'''
def backtrack(item_list,capacity):
    max_value=0
    stack=[(0,0,0)]
    prev_weight=int(prev_weight)
    prev_value=int( prev_value)

    while stack:
        index,prev_weight.itemweight,prev_value.itemvalue=stack.pop()
        
        if index == len(item_list):
           if prev_value > max_value:
              max_value = prev_value
              
        else:
            stack.append((index + 1, prev_weight, prev_value))
            print(stack)
            # Include the current item if within capacity
            new_weight = prev_weight + prev_weight.itemweight
            new_value = prev_value + prev_value.itemvalue
            if new_weight <= capacity:
                stack.append((index + 1, new_weight, new_value))
                #print(stack)
        return max_value       
        '''
'''
for i in item_list:
    #for j in i:
        w = i.itemweight
        if w <= capacity:
           #v = i.itemvalue
           max_value += i.itemvalue
           print(f"Maximum value is: {max_value}")
     '''

max_value = 0
best_combination = []

def backtrack(index, current_items, current_weight, current_value):
    global max_value, best_combination

    # If total weight exceeds capacity, backtrack
    if current_weight > capacity:
        return

    # If we've processed all items
    if index == len(item_list):
        if current_value > max_value:
            max_value = current_value
            best_combination = current_items[:]
        return

    # Include the current item
    current_items.append(item_list[index])
    backtrack(index + 1,
              current_items,
              current_weight + item_list[index].itemweight,
              current_value + item_list[index].itemvalue)
    current_items.pop()

    # Exclude the current item
    backtrack(index + 1,
              current_items,
              current_weight,
              current_value)

# Start the recursion
backtrack(0, [], 0, 0)

# Print the result
print("Best combination:")
for item in best_combination:
    print(f"{item.itemname}: Weight={item.itemweight}, Value={item.itemvalue}")
print(f"Total Value: {max_value}")

#print(backtrack(item_list,capacity))



