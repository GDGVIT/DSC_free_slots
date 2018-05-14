# -*- coding: utf-8 -*-
"""
Created on Mon May  7 10:30:08 2018

@author: parit
"""

from PIL import Image

import numpy as np
a = Image.open('paritosh.png')
a = np.array(a)
lab_free = [249,239,164,255]
theory_free = [255,255,204,255]
busy = [204,255,51,255]
break_color = [60,141,188,255]

flag = 0
#i refers to columns of image and j refers to rows

num_col = len(a)
num_row = len(a[0])

for i in range(num_col):
    for j in range(num_row):
        
        if((a[i][j]==theory_free).all() or (a[i][j]==lab_free).all() or (a[i][j]==busy).all()):
            
            flag = 1
            break
    if(flag == 1):
        break
  
         
    
        
free = [] # this contains the free slots . the slot number goes from 1-65 (vertically and then horizontally)
#
classes = []
class_type = [] #0 for theory , 1 for lab
L = 0
first = 1
updated = 0
for l in range(j,num_row):
    
    if(first == 1):
        theory_flag = 1
        
        if(updated == 0):
            L+=1
    #if(first == 1 and ((a[k][j]==theory_free).all() or (a[k][j]==lab_free).all() or (a[k][j]==busy).all())):
        
        for k in range(i,num_col):
            #print(k,l,a[k][l])
            
            if(theory_flag == 1):
            
                if((a[k][l]==busy).all() ):
                    #print("theory busy",k,l)
                    th = 0
                    if(L not in classes):
                        classes.append(L)
                        class_type.append(0)
                   
                elif((a[k][l]==theory_free).all()):
                    #print("theory empty",k,l)
                    th = 1
                
                elif((a[k][l]==break_color).all()):
                        #print("theory complete",k,l)
                        theory_flag = 0
                
                
                
            else:
                
                updated = 0
                if((a[k][l]==busy).all()):
                    #print("lab busy",k,l)
                    if(L not in classes):
                        classes.append(L)
                        class_type.append(1)
                    lab = 0
                    
                    
                elif((a[k][l]==lab_free).all()):
                    #print("lab empty",k,l)
                    lab = 1
                    if(th == 1):
                        if(L not in free):
                            free.append(L)
                        
                elif((a[k][l]==break_color).all() ):
                    
                        
                        #print("lab complete",k,l)
                        theory_flag = 1
                        if(L%5==0):
                            break
                        else:
                            L+=1
                        
                            updated = 1
                    
                     
                
        first = 0
    else:
        if((a[i][l]==break_color).all() and ((a[i][l+1]==theory_free).all() or (a[i][l+1]==busy).all())):
            first = 1
            
        
    #else:
     #   if ( (a[k-1][j]==break_color).any() and ((a[k][j]==theory_free).all() or (a[k][j]==busy).all())):
      #       first = 1
            
sure_free = [26,27,28,29,30,61,62,63,64,65]   

for e in sure_free:
    if(e not in free):
        free.append(e)
            
import json

with open('data.txt') as json_file:  
    data = json.load(json_file)
    
data["paritosh"] = free

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)
# For checking the classes and its class type ( 0 for theory and 1 for lab )            
print(classes,class_type)       
        
#a has 768 columns as another array in a

