# -*- coding: utf-8 -*-
"""
Created on Sun May 13 20:06:17 2018

@author: parit

time to slot
"""
import json
import math
with open('data.txt') as json_file:  
    data = json.load(json_file)
    L = (data["paritosh"])
#L=[16, 18, 20, 22, 26, 27, 28, 29, 30, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 50, 51, 52, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 65]
# include values 21-25 and 61-65
time = [8,9,10,11,12,13,14,15,16,17,18,19,20] 
mon=[]
tue=[]
wed=[]
thu=[]
fri=[]

for slot in L:
    index = math.ceil(slot/5) - 1
    if(slot % 5 == 1):
        mon.append (time[index])
        #monday
        
        
    elif(slot % 5 == 2):
         tue.append (time[index])
        #tuesday
    elif(slot % 5 == 3):
         wed.append (time[index])
        #wednesday
    elif(slot % 5 == 4):
         thu.append (time[index])
        #thursday
    else:
         fri.append (time[index])
        #friday


#slots = {}  
with open('slots.txt') as json_file:  
    slots = json.load(json_file)
slots["paritosh"]=[]
slots['paritosh'].append({  
    'mon': mon,
    'tue': tue,
    'wed': wed,
    'thu': thu,
    'fri': fri
})

with open('slots.txt', 'w') as outfile:  
    json.dump(slots, outfile)
