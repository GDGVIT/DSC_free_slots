# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:43:44 2018

@author: parit
"""
import json
with open('slots.txt') as json_file:  
    slots = json.load(json_file)
    
name = "paritosh"
day = "tue"
time_from = 14
time_to = 19
reqd_time = []


for i in range(time_from, time_to):
    reqd_time.append (i)

hrs = time_to - time_from

# Finding the free slots of a particular person on given day

reqd_day_free_slots = slots[name][0][day]

start_temp = reqd_day_free_slots[0]
temp = start_temp
for time in reqd_day_free_slots:
    
        
    print(time,"-",time+1)
    
#finding the name of the person who is free in a given time interval
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
    
    
    