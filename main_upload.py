# -*- coding: utf-8 -*-
"""
Created on Sun May 20 13:31:02 2018

@author: parit

main_upload_screenshots
"""
from screenshotAnalyzer import convertImage2json
from slotToTime import convertSlotToTime
import os

#       Pass the address of program folder
def main(folderAddress):
    
    os.chdir(folderAddress+"test\\test images")
    files=[]

    #       Add all the filenames present in the folder to the list - 'files'
    
    for name in os.listdir('.'):
        files.append(name)
    
    os.chdir(folderAddress)
    for filename in files:
        
        #    this will extract the slotNumbers from the screenshots and save it in slotNumbers.txt in json format
        convertImage2json( filename )
        
    #      Convert the self defined free slot numbers , into Day and Time details and store it in day&time.txt in json     
    convertSlotToTime()
    
        

#   ---------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    
    main("C:\\Users\\parit\\DSC_free_slots\\")
    
    
    
    
    