# -*- coding: utf-8 -*-
"""
Created on Wed May 14 21:03:26 2025

@author: hp
"""

class item_detail:
    def __init__(self,itemname,itemweight,itemvalue,identity):
        self.itemname = itemname
        self.itemweight = itemweight
        self.itemvalue = itemvalue
        self.identity = identity
        self.value_per_unit_weight = itemvalue/itemweight
    




