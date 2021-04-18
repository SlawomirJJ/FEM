import numpy as np
import random as r



def GenerujTabliceGeometrii (x_range):
    print('Zapisz liczbę węzłów')
    nodes_num = int(input())
    
    val = (x_range[1]-x_range[0])/(nodes_num-1)
    nodes = np.array([x_range[0]])
    
    for i in range(1,nodes_num):
        nodes = np.block([nodes, i * val + x_range[0]])
    for i in range(1,nodes_num-1):
        nodes[i] = nodes[i] + round(r.uniform(-0.05, 0.05),2)
    nodes = np.around(nodes, decimals=2)
    
    sections = np.zeros((nodes_num-1,2))


    for i in range(0, nodes_num-1, 1):
        sections[i][0] = i
        sections[i][1] = i+1

    return nodes, sections

print(GenerujTabliceGeometrii(1))

