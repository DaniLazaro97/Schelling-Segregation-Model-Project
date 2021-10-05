'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''

'''Unhappy and Empty list generator'''

import numpy as np


def unhappy_and_empty_info_extraction_for_policies(segregation_intmap, happiness_map, k, p):

    l_side = segregation_intmap.shape[0]
    w = int((p-1)/2)
    unhappy_info = []
    empty_info = []
    unhappy_coords = find_coords(happiness_map, -1)
    empty_coords = find_coords(segregation_intmap, 0)
    
    for coords in unhappy_coords:
        race = int(segregation_intmap[coords[0],coords[1]])
        n_reds = 0
        n_blues = 0
        i = coords[0]
        j = coords[1]
        for k in list(range(i-w, i+w+1)): #change of coordinates 
            k_hat = coord_change(k,l_side)
            for l in list(range(j-w, j+w+1)):
                l_hat = coord_change(l,l_side) 
                count_condition = [i,j] != [k,l] #we don't want to count the center cell [i,j]
                if count_condition:
                    #remember, in the segregation intmap: 0=empty, 1=blue, 2=red
                    if segregation_intmap[k_hat, l_hat] == 1:
                        n_blues += 1
                    elif segregation_intmap[k_hat, l_hat] == 2:
                        n_reds += 1
                    else: #if there is an empty spot red and blue counters won't update
                        pass
                    
        info_coord = [coords, n_blues, n_reds, race]
        unhappy_info.append(info_coord)
        
    for coords in empty_coords:
        n_reds = 0
        n_blues = 0
        i = coords[0]
        j = coords[1]
        for k in list(range(i-w, i+w+1)): #change of coordinates 
            k_hat = coord_change(k,l_side)
            for l in list(range(j-w, j+w+1)):
                l_hat = coord_change(l,l_side) 
                count_condition = [i,j] != [k,l] #we don't want to count the center cell [i,j]
                if count_condition:
                    #remember, in the segregation intmap: 0=empty, 1=blue, 2=red
                    if segregation_intmap[k_hat, l_hat] == 1:
                        n_blues += 1
                    elif segregation_intmap[k_hat, l_hat] == 2:
                        n_reds += 1
                    else: #if there is an empty spot red and blue counters won't update
                        pass
                    
        info_coord = [coords, n_blues, n_reds]
        empty_info.append(info_coord)
        
    return unhappy_info, empty_info


def find_coords(any_map, value): #returns a list with the coordinates of the desired value that you are looking for

    coords_unzipped = np.where(any_map == value)
    coords_zipped = zip(list(coords_unzipped[0]),list(coords_unzipped[1])) #this returns a list of tuples with the coordinates
    coords = [list(i) for i in list(coords_zipped)] #the a list of coordinates as lists

    return coords

def coord_change(i,l):
    
    i = i%l
    
    return i

