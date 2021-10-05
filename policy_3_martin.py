'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''

'''Selfish Social Network: Jon Ander Martin'''

from unhappy_and_empty_lists import unhappy_and_empty_info_extraction_for_policies
from friendship import agent_and_friends_coords
from random import shuffle
from happiness import happiness, coord_change

def neighborhood_coords_search_martin(coords_friends, intmap,k,p): 
    #this function finds all the coordinates of the neighbors of the friends
    
    #we are going to return all those coordinates in a list
    #empty and not empty spots, because the agents move one at a time
    #that means that if one moves and leaves an empty spot that spot could be neighbor of a friend of the 
    #next agent that moves...
    
    l = intmap.shape[0]
    
    l_side = l
    w = int((p-1)/2)
    neighbor_coords = []
    neighbor_class = []
    counter = 0
    for coords in coords_friends:
        i = coords[0]
        j = coords[1]

        for k in list(range(i-w, i+w+1)): #change of coordinates 
                k_hat = coord_change(k,l_side)
                for l in list(range(j-w, j+w+1)):
                    l_hat = coord_change(l,l_side)
                    append_condition =  [i,j] != [k_hat,l_hat] and not [k_hat,l_hat] in neighbor_coords
                    #we don't want to count the center cell [i,j]
                    if append_condition:
                        neighbor_coords.append([k_hat, l_hat])
                        neighbor_class.append(intmap[coords_friends[counter][0],coords_friends[counter][1]])
                    
        counter += 1
    
    return neighbor_coords, neighbor_class

def relocation_policy3_martin(segregation_intmap, happiness_map, id_map, k, p, p_friends, q, n_friends):
    
    unhappies, empties = unhappy_and_empty_info_extraction_for_policies(segregation_intmap, happiness_map, k, p)
    shuffle(unhappies)
    for unhappy in unhappies:

        coords_unhappy = unhappy[0]
        id_unhappy = id_map[0, coords_unhappy[0], coords_unhappy[1]]
        race_unhappy = unhappy[-1]
        
        _, coords_friends, id_friends = agent_and_friends_coords(id_unhappy, id_map, n_friends)
        coords_neighbors, class_neighbors = neighborhood_coords_search_martin(coords_friends, segregation_intmap, k, p_friends)

        #those are the coords of all the spots that belong to the unhappy's friends' neighborhood 
        #first let's check that there is any potential spot for the unhappy, we will compare the lists 
        #coords_neighbors and empties(the coords) obtaining only the potential empty spots
        neighbor_empties = [empty_info for empty_info in empties if empty_info[0] in coords_neighbors] #coords of the empty list spots
        class_empties = []
        empties_coords = []
        for v in range(len(empties)):
            empties_coords.append(empties[v][0])
        for v in range(len(coords_neighbors)):
            coord = coords_neighbors[v]
            if coord in empties_coords:
                class_empties.append(class_neighbors[v])
            
        #we check if there is any
        search_happy = False
        if len(neighbor_empties) > 0:
            search_happy = True   
        else:
            pass
        
        #if there are empty spots we search for one makes the agent happy    
        move_condition = False
        index_new_spot = 0
        
        if search_happy:
            random_idx = list(range(len(neighbor_empties)))
            shuffle(random_idx)
            # shuffle(neighbor_empties) #it has to be a random search
            
            while ((not move_condition) and (index_new_spot < len(neighbor_empties))):
                
                empty = neighbor_empties[random_idx[index_new_spot]]
                if empty[int(class_empties[random_idx[index_new_spot]])] >= k:
                    move_condition = True 
                    new_spot = neighbor_empties[random_idx[index_new_spot]]
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
                    
                    
                
            