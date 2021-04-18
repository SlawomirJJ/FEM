import numpy as np
import random as r



def GenerujTabliceGeometrii (x_range):
    print('Zapisz liczbę węzłów')
    li_WEZLY = int(input())
    
    val = (x_range[1]-x_range[0])/(li_WEZLY-1)
    WEZLY = np.array([x_range[0]])
    
    for i in range(1,li_WEZLY):
        WEZLY = np.block([WEZLY, i * val + x_range[0]])
    for i in range(1,li_WEZLY-1):
        WEZLY[i] = WEZLY[i] + round(r.uniform(-0.05, 0.05),2)
    WEZLY = np.around(WEZLY, decimals=2)
    
    sections = np.zeros((li_WEZLY-1,2))


    for i in range(0, li_WEZLY-1, 1):
        sections[i][0] = i
        sections[i][1] = i+1

    return WEZLY, sections


