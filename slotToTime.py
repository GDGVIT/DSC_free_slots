# -*- coding: utf-8 -*-
"""
Created on Sun May 13 20:06:17 2018

@author: parit

time to slot
"""
def store2json (name, days):
    
    import json
    with open('day&time.txt') as json_file:  
        hours = json.load(json_file)
        hours[name]=[]
        hours[name].append({  
            'mon': days[0], #mon
            'tue': days[1], #tue
            'wed': days[2], #wed
            'thu': days[3], #thu
            'fri': days[4]  #fri
        })
    
    with open('day&time.txt', 'w') as outfile:  
        json.dump(hours, outfile)

#-----------------------------------------------------------------------------------------------------
        
def convertSlotToTime():
    
    import json
    import math
    with open('slotNumbers.txt') as json_file:  
        data = json.load(json_file)
        
    time = [8,9,10,11,12,13,14,15,16,17,18,19,20]  # It contains the hours of the day 
    
    for name in data:      #   Loop through FreeSlotNumbers of each member 
        L = data[name]        
        #    Daywise list of free slots 
        mon = []
        tue = []
        wed = []
        thu = []
        fri = []
        
        # Converting slot to number to day and time , using the slot number assumption done in this program
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
        #    List containing the details of all the days
        
        days = [mon, tue, wed, thu, fri]
        
        # Store the data in day&time.txt in json format
        store2json (name, days )
         

        
