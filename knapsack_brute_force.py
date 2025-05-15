#Second is weight
#First is value
#items={'item1':(8,6),'item2':(2,4),'item3':(5,9),'item4':(6,3),'item5':(4,1)}
capacity=15
from itertools import combinations
from oops_concepts import item_detail 
a=item_detail('item1',6,8,1)
b=item_detail('item2',4,2,2)
c=item_detail('item3',9,50,3)
d=item_detail('item4',3,6,4)
e=item_detail('item5',1,4,5)

items=[a,b,c,d,e]
item_dict={}
for i in items:
    item_dict[i.identity]= i
    
    
allcombination=[]
for r in range(1,len(items)+1):
    for combination in combinations(items,r):
        allcombination.append(combination)
        
#print(lenallcombination))
eligiblecombination=[]
for i in allcombination:
    total_weight=0 
    for j in i:
            w = j.itemweight
            total_weight+=w
    if total_weight<=capacity:
       eligiblecombination.append(i)
#print(len(eligiblecombination))  

max_value = -1
for k in eligiblecombination :
    value=0
    for z in k:
        v = z.itemvalue
        value += v
    if value > max_value:
       max_value = value
       bestcombo=k
       
print(max_value)
[print(i.itemname )for i in bestcombo]
  
#print(eligiblecombination)
#print(len(eligiblecombination))
#print(len(allcombination))
        
    



