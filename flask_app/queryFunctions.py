# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:43:44 2018

@author: parit
"""

# Finding the free slots of a particular person on given day
def free_hrs(member, free_users, reqd_time,day):
    """ print the free hours of the required person """
    result = {}
    name = member[0]
    free_hrs = member[1]
    result["name"] = name
    result["free_hrs"] = free_hrs;
    result["timings"] = {}
    result["timings"]["time_slots"]=[]
    result["timings"]["container_nos"]=[]
    reqd_time_avail = free_users[name]
    for i in range(len(reqd_time_avail)):
        temp = ""
        if(reqd_time_avail[i] == 1):
            temp = temp + str(reqd_time[i])+ "-" + str(reqd_time[i] + 1)
            result["timings"]["time_slots"].append(temp)
            result["timings"]["container_nos"].append(hrsToSlot(reqd_time[i],day))
    return result

def findFreeSlots(name, day, slots):
    """ Find the free slots of the required member from the club """
    reqd_day_free_slots = slots[day] #  Array containing the free hours of the member
    # the below loop displays the collective free slots of the given member

    slot_details = {}
    slot_details["name"] = name;
    slot_details["free_hrs"] = len(reqd_day_free_slots)
    slot_details["slots"] = []
    for i in reqd_day_free_slots:
        slot_details["slots"].append(hrsToSlot(i,day))
    timings = []
    for hour in reqd_day_free_slots:
        temp = ""
        temp = temp + str(hour) + "-" + str(hour + 1)
        timings.append(temp)
    slot_details["timings"] = timings
    return slot_details

    """for index in range(0,len(reqd_day_free_slots)):
   
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
"""
#------------------------------------------------------------------------------
def slotToHrs(slot_no):
    import math
    reqd_time = []
    for slot in slot_no:
        index = math.ceil(slot/5) - 1 + 8
        reqd_time.append(index)
    reqd_time.sort()
    return reqd_time

def hrsToSlot(hrs,day):
    if(day == "mon"):
        i = 1
    elif(day == "tue"):
        i = 2
    elif(day == "wed"):
        i = 3
    elif(day == "thu"):
        i = 4
    elif(day == "fri"):
        i = 5
    slot = (hrs - 8)*5 + i
    return slot
        
def findFreeMembers(slot_no, day, slots):
    """finding the name of the person who is free in a given time interval """

    free_users = {}  #contain the member names with their corresponding availability during reqd slots
    users_free_count = {} #    will contain number of hours the member is free in that duration
   

    reqd_time = slotToHrs(slot_no)
    for user_name in slots:

        reqd_time_avail = []
        avail = slots[user_name][day]
        for item in reqd_time:

            if(item in avail):
                reqd_time_avail.append(1)
            else:
                reqd_time_avail.append(0)

        free_users[user_name] = reqd_time_avail
        users_free_count[user_name] = reqd_time_avail.count(1)

#   Sorting the users_free_count dictionary in decreasing order by value, so that the 
#   member with most number of free hours come first

    sorted_list = [x for x in users_free_count.items()]
    sorted_list.sort(key=lambda x: x[1]) #sort by value
    sorted_list.reverse()

#   Displaying the result to user
    noMemberFree = 1
    freeMembers =[]
    for member in sorted_list:
        
        if(member[1] > 0):
            noMemberFree = 0
            freeMembers.append(free_hrs(member, free_users, reqd_time, day))
            #if(member[1] == len(slot_no)):
                #print(member[0])
            #else:
                #print(member[0], " Available hrs(", member[1], "): ", end=" ")
                
        

    if(noMemberFree == 1):
        print("Aw snap! I didn't find anyone free during this interval")
    return freeMembers

