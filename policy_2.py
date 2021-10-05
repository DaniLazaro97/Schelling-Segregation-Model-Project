'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''

'''Policy 2'''

from unhappy_and_empty_lists import unhappy_and_empty_info_extraction_for_policies
from friendship import agent_and_friends_coords, neighborhood_coords_search
from random import shuffle
from happiness import happiness

def relocation_policy2(segregation_intmap, happiness_map, id_map, k, p, p_friends, q, n_friends):
    
    unhappies, empties = unhappy_and_empty_info_extraction_for_policies(segregation_intmap, happiness_map, k, p)
    shuffle(unhappies)
    for unhappy in unhappies:

        coords_unhappy = unhappy[0]
        id_unhappy = id_map[0, coords_unhappy[0], coords_unhappy[1]]
        race_unhappy = unhappy[-1]
        
        _, coords_friends, id_friends = agent_and_friends_coords(id_unhappy, id_map, n_friends)
        coords_neighbors = neighborhood_coords_search(coords_friends, segregation_intmap.shape[0], k, p_friends)

        #those are the coords of all the spots that belong to the unhappy's friends' neighborhood 
        #first let's check that there is any potential spot for the unhappy, we will compare the lists 
        #coords_neighbors and empties(the coords) obtaining only the potential empty spots
        neighbor_empties = [empty_info for empty_info in empties if empty_info[0] in coords_neighbors] #coords of the empty list spots
        
        #we check if there is any
        search_happy = False
        if len(neighbor_empties) > 0:
            search_happy = True
            
        else: pass
        #if there are empty spots we search for one makes the agent happy    
        move_condition = False
        index_new_spot = 0
        
        if search_happy:
            shuffle(neighbor_empties) #it has to be a random search
            
            while ((not move_condition) and (index_new_spot < len(neighbor_empties))):
                
                empty = neighbor_empties[index_new_spot]
                if empty[race_unhappy] >= k:
                    move_condition = True 
                    new_spot = neighbor_empties[index_new_spot]
                    new_spot_coords = new_spot[0]
                    
                else: index_new_spot += 1
            
            if move_condition:
                #update segregation Intmap
                segregation_intmap[new_spot_coords[0],new_spot_coords[1]] = race_unhappy #new spot
                segregation_intmap[coords_unhappy[0],coords_unhappy[1]] = 0 #old spot
                #update id map: move the id of the unhappy and his friends
                for i in range(n_friends+1):
                    id_map[i, coords_unhappy[0], coords_unhappy[1]] = 0 #old spot
                    if i == 0: 
                        id_map[i, new_spot_coords[0], new_spot_coords[1]] = id_unhappy #new spot
                    else:
                        id_map[i, new_spot_coords[0], new_spot_coords[1]] = id_friends[i-1] #new spot
                #update the empty list:
                for i in range(0, len(empties)):
                    
                    caca = empties[i]
                    if caca[0] == [new_spot_coords[0],new_spot_coords[1]]:
                        empties.pop(i)
                        break
                    
                
                new_empty_spot = unhappy
                new_empty_spot.pop(3)
                empties.append(new_empty_spot)
                happiness_map = happiness(segregation_intmap, k, p)
                unhappies1, empties = unhappy_and_empty_info_extraction_for_policies(segregation_intmap, happiness_map, k, p)
        
                counter = 0
                for unhappy in unhappies:
                    for unhappy1 in unhappies1:
                        if unhappy[0] == unhappy1[0]:
                            unhappies[counter] = unhappy1
                    counter +=1
                
            else: pass
        else: pass
            
    happiness_map = happiness(segregation_intmap, k, p)
    
    return segregation_intmap, happiness_map, id_map
                    
                    
                
            