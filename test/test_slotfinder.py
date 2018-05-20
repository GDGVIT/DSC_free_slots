# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:10:05 2018

@author: parit
"""
import os
import unittest

os.chdir("..")


from screenshotAnalyzer import findFirstBlock, convertImage2json
from slotToTime import convertSlotToTime
import numpy as np
from PIL import Image

class TestFreeSlots(unittest.TestCase):

    def test_screenshotAnalyzer(self):
        
        freeSlots = convertImage2json("paritosh.png")
        
        assert ( len(freeSlots) > 15 )
    
    def test_findFirstBlock(self):
        
        lab_free = [249,239,164,255]
        theory_free = [255,255,204,255]
        busy = [204,255,51,255]
        break_color = [60,141,188,255]
        colors = [lab_free, theory_free, busy, break_color]
        a = Image.open("test\\test images\\paritosh.png" )
        a = np.array (a)
        pos = findFirstBlock ( a , colors)
        
        assert pos[1]<len(a) - 1
        #assert pos[0]<len(a[0]) - 1

if __name__ == "__main__":
    
    unittest.main()