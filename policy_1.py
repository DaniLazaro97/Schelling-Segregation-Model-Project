'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''

'''Policy 1'''

from random import shuffle

from unhappy_and_empty_lists import unhappy_and_empty_info_extraction_for_policies
from happiness import happiness

def relocation_policy1(segregation_intmap, happiness_map, k, p, q):
    
    unhappies, empties = unhappy_and_empty_info_extraction_for_policies(segregation_intmap, happiness_map, k, p)
    #we want this process to be random so we shuffle the list
    shuffle(unhappies)

 
    for unhappy in unhappies:
        
        shuffle(empties)
        #now we pick q empties
        empties_q =  empties[0:q]
        
        coords_unhappy = unhappy[0]
        race_unhappy = int(unhappy[3]) #race can be 1 or 2 that is the same value of the indexes of
        # the n_blues and n_reds information
        found_happy_spot = False
        #let's find a happy spot
        i = 0
        less_unhappy_spot = unhappy #initialize the vble that searches for the less unhappy spot
        found_less_unhappy_spot = False

        while i < q and not found_happy_spot:       
            empty = empties_q[i]
                        
            if empty[race_unhappy] >= k: #check if that empty is happy

                found_happy_spot = True
                new_empty_spot = unhappy
                new_empty_spot.pop(3)
                index_happy = i
                happy_spot = empty
                #print(empties[i])
                
            else:
                if less_unhappy_spot[race_unhappy] < empty[race_unhappy]:

                    less_unhappy_spot = empty
                    index_less_unhappy = i
                    found_less_unhappy_spot = True
            
            if i<q:
                i += 1
            else:
                pass
            
        if not found_happy_spot and found_less_unhappy_spot:

            new_coords = less_unhappy_spot[0] #coords of the least unhappy
            segregation_intmap[new_coords[0], new_coords[1]] = race_unhappy #update segregation map
            segregation_intmap[coords_unhappy[0], coords_unhappy[1]] = 0
            empties.pop(index_less_unhappy)
            new_empty_spot = unhappy
            new_empty_spot.pop(3)
            empties.append(new_empty_spot)
            
            
        elif found_happy_spot:
            new_coords = happy_spot[0]
            segregation_intmap[new_coords[0],new_coords[1]] = race_unhappy
            segregation_intmap[coords_unhappy[0], coords_unhappy[1]] = 0
            empties.pop(index_happy)
            empties.append(new_empty_spot)
            
        else:
            pass
        
        happiness_map = happiness(segregation_intmap, k, p)
        unhappies1, empties = unhappy_and_empty_info_extraction_for_policies(segregation_intmap, happiness_map, k, p)
        
        counter = 0
        for unhappy in unhappies:
            for unhappy1 in unhappies1:
                if unhappy[0] == unhappy1[0]:
                    unhappies[counter] = unhappy1
            counter +=1
            
 
            
    happiness_map = happiness(segregation_intmap, k, p)
    
    return segregation_intmap, happiness_map        




