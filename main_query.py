# -*- coding: utf-8 -*-
"""
Created on Sun May 20 15:11:17 2018

@author: parit

main_query
"""
from queryFunctions import findFreeMembers, findFreeSlots
import json

if __name__ == "__main__" :
    
    print("\t\tWelcome to the free Slot Finder\n")
    
    print("What you want me to query ? Enter the corresponding number")
    print("1 -> Find members who are free during some time interval")
    print("2 -> Find the free slots of a particular member on a specific day")
    
    choice = int(input())
    
    with open('day&time.txt') as json_file:  
        hours = json.load(json_file)
        
    if(choice == 1):
        day = input("Day(First 3 letters): ")
        time_from = int(input("From(24 hr clock): "))
        time_to = int(input("To: "))

        findFreeMembers(time_from, time_to, day, hours)
        
    else:
        
        name = input("Member name: ")
        day = input("Day(First 3 letters): ")
        
        findFreeSlots(name, day, hours)