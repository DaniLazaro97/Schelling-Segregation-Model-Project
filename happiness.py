'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''

'''Happiness map'''

import numpy as np

#Calculates the happiness map (happiness of every agent) from the segregation information 
#stored in the segregation_intmap variable
def happiness(segregation_intmap, k, p):
    
    happiness_map = np.zeros_like(segregation_intmap)
    l_side = segregation_intmap.shape[0]
    k_same = k
    w = int((p-1)/2)
    for i in range(0, l_side):
        for j in range(0, l_side):
            
            n_sameclass = 0
            class_current = segregation_intmap[i,j]
            
            ## search neighbors and count matching class agents, only if the
            ## current cell is not empty
            if class_current != 0:
                for k in list(range(i-w, i+w+1)): #change of coordinates 
                    k_hat = coord_change(k,l_side)
                    for l in list(range(j-w, j+w+1)):
                        l_hat = coord_change(l,l_side)
                        happy_condition = segregation_intmap[k_hat,l_hat] == class_current and [i,j] != [k_hat,l_hat] 
                        #we don't want to count the center cell [i,j]
                        if happy_condition:
                            n_sameclass += 1  
                        
                if n_sameclass >= k_same:
                    happiness_map[i,j] = 1
                else:
                    happiness_map[i,j] = -1
                    
            else:  # current cell is empty
                pass
            
    return happiness_map

def coord_change(i,l):
    
    i = i%l
    
    return i

