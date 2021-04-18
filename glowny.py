# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:08:53 2021

@author: Sławomir Jedziniak
"""

import numpy as np
import random as r
import sys 
import matplotlib.pyplot as plt


#parametry sterujące
c=0
f=0


#geometria
x_a = 0
x_b = 1



#n=4
print(x_a)


WEZLY = np.array([[1,0],
                 [2,1],
                 [3,0.5],
                 [4,0.75]])




ELEMENTY =np.array([[1,1,3],
                    [2,4,2],
                    [3,3,4]])



print(ELEMENTY)

# warunki brzegowe 
twb_L='D'
twb_P='D'
wwb_L=0
wwb_P=1



x_range, conditions, types = MacierzWsp([-1,2,-1,3,'N','D'])
print('x range', x_range)
print('conditions', conditions)
print('types', types)
#1b
WEZLY, sections = GenerujTabliceGeometrii(x_range)
print('WEZLY', WEZLY)
print('sections', sections)
#1c
RysujGeom(x_range, WEZLY,types)









