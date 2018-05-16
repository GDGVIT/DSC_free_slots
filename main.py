# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:43:44 2018

@author: parit
"""

# Finding the free slots of a particular person on given day

def findFreeSlots(name, day, slots):
    
    reqd_day_free_slots = slots[name][0][day]    #  Array containing the free hours of the member
    
    # the below loop displays the collective free slots of the given member
    
    for index in range(0,len(reqd_day_free_slots)):
        
        if(index == 0):
            
            start_temp = reqd_day_free_slots[0]          #  The first free hour of the day
            temp = start_temp
        else:
            
            if(reqd_day_free_slots[index] - reqd_day_free_slots[index-1] == 1 and index != len(reqd_day_free_slots) - 1):
            
                temp = reqd_day_free_slots[index]
            
            else:
            
                print(start_temp, "-", temp + 1)
                start_temp = reqd_day_free_slots[index] 
                temp = reqd_day_free_slots[index]

#------------------------------------------------------------------------------
        
#finding the name of the person who is free in a given time interval
        
def findFreeMembers(time_from, time_to, day, slots):
    
    free_users={}    
    for user_name in slots:
        reqd_time_avail=[]
        avail = slots[user_name][0][day]
    for item in reqd_time:
        if(item in avail):
            reqd_time_avail.append(1)
        else:
            reqd_time_avail.append(0)
        
    free_users[user_name] = reqd_time_avail
    free_usernames = []
    while(hrs>0):
        for name in free_users:
            if(free_users[name].count(1) == hrs):
                free_usernames.append(name)
                hrs-=1
    print(name)
    
#------------------------------------------------------------------------------



if __name__ == "__main__":    
    
    import json
    with open('slots.txt') as json_file:  
        slots = json.load(json_file)
    
    name = "paritosh"
    day = "mon"
    time_from = 14
    time_to = 19
    reqd_time = []


    for i in range(time_from, time_to):
        reqd_time.append (i)

    hrs = time_to - time_from
    
    findFreeSlots(name, day, slots)




    


    
    
    